# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:24:47 2021

@author: Molinari
"""
import numpy as np
#from osgeo import gdal
import subprocess as sp
import os
from PIL import Image
from rasterio.fill import fillnodata
from scipy import ndimage
import rasterio

np.warnings.filterwarnings('ignore')


filepath=r"C:/Users/Molinari/Dropbox (DEIB)/MONIA/TWIGA/SUDAFRICA_2018/Diff_APS/20180402163741_APS_MM_ZENITH_MERGED.tif"

f=filepath.split("/")[-1]

filepath_tif = filepath.split(f)[0]+"NEW.tif"
filepath_jpg = filepath.split(".tif")[0]+".jpg"
filepath_mask = filepath.split(".tif")[0]+"_mask.gif"


# Open GTiff
src = rasterio.open(filepath)
arr=src.read(1)
cols=arr.shape[1]
rows=arr.shape[0]


np.nanmin(arr)
np.nanmax(arr)

# Compute percentiles and rescale
percentile_1 = np.nanpercentile(arr, 1)
percentile_99 = np.nanpercentile(arr, 99)

arr[arr > percentile_99] = percentile_99
arr[arr < percentile_1] = percentile_1

# If percentile_1 negative, rescale to 0
if percentile_1<0:
    arr=arr+abs(percentile_1)
    
    
# Create mask for taking account of nan (0=nan; 255=others)
mask_arr =  np.zeros_like(arr)
mask_arr[arr>=0]=255
image_pil = Image.fromarray(mask_arr.astype(np.uint8))
image_pil.save(filepath_mask)

    
# Fill NODATA
arr_filled = fillnodata(arr, mask=mask_arr, max_search_distance=1000, smoothing_iterations=0)

#  Smoothing
arr_smooth = ndimage.gaussian_filter(arr_filled,sigma=2)

# Rescale from 0 to 255
amin=np.nanmin(arr_smooth)
amax=np.nanmax(arr_smooth)

arr_rescaled = (np.round((((arr_smooth-amin) / (amax-amin) * 255)+amin))).astype(np.uint8)
scaleX1=(amax-amin)/255
scaleX2 = amin


# Create rescaled GTiff
profile = src.profile.copy()
profile.update(
   dtype='uint8'
    )

with rasterio.open(filepath_tif, 'w', **profile) as dst:
     dst.write(arr_rescaled,indexes=1)
     dst.update_tags(Percentile_1= percentile_1)
     dst.update_tags(SCALE_X1=scaleX1)
     dst.update_tags(SCALE_X2=scaleX2)


# Convert GTiff to JPEG
cmd = ['gdal_translate', '-of', 'JPEG', '-co', 'worldfile=yes', filepath_tif,filepath_jpg]
sp.check_call(cmd, shell=True)

# Remove rescaled GTiff
os.remove(filepath_tif)