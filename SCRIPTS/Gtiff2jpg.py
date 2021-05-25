# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:24:47 2021

@author: Molinari
"""

import subprocess as sp
import os
from PIL import Image
from rasterio.fill import fillnodata
from scipy import ndimage
import rasterio
import argparse
import numpy as np
np.warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser(description='GeoTIFF to JPEG conversion')
parser.add_argument('input', type=str,
                   help='GeoTIFF image')

# Get input argument
args = parser.parse_args()
filepath = args.input
print("\nConversion of %s started...\n"%filepath)

# Define temporary and output files
f=filepath.split("/")[-1]
filepath_tif = filepath.split(f)[0]+"NEW.tif"
filepath_jpg = filepath.split(".tif")[0]+".jpg"
filepath_mask = filepath.split(".tif")[0]+"_mask.gif"

# Remove existing output files
if os.path.isfile(filepath_jpg):
    os.remove(filepath_jpg)

if os.path.isfile(filepath_jpg.split("jpg")[0] +"wld"):
    os.remove(filepath_jpg.split("jpg")[0] +"wld")

if os.path.isfile(filepath_jpg +".aux.xml"):
    os.remove(filepath_jpg +".aux.xml")

if os.path.isfile(filepath_mask):
    os.remove(filepath_mask)

# Open GTiff
src = rasterio.open(filepath)
arr=src.read(1)
cols=arr.shape[1]
rows=arr.shape[0]


np.nanmin(arr)
np.nanmax(arr)

# Compute cut values and rescale image
nan_array = np.isnan(arr)
not_nan_array = ~ nan_array
array2cut = np.sort(arr[not_nan_array])

percentile_1 = array2cut[20]
percentile_99 = array2cut[-20]

#percentile_1 = np.nanpercentile(arr, 0.1)
#percentile_99 = np.nanpercentile(arr, 99.9)

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
print("...NODATA filled.\n")

#  Smoothing
arr_smooth = ndimage.gaussian_filter(arr_filled,sigma=2)
print("...Smoothing performed.\n")

# Rescale from 0 to 255
amin=np.nanmin(arr_smooth)
amax=np.nanmax(arr_smooth)
min_des=0

arr_rescaled_f = np.around((min_des +  ((arr_smooth-amin) / (amax-amin)) * 255))
arr_rescaled = arr_rescaled_f.astype(np.uint8)


scaleX1=(amax-amin)/255
scaleX2 = min_des


# Create rescaled GTiff
profile = src.profile.copy()
if profile['nodata']!=None:
    if profile['nodata']<0 or profile['nodata']>255:
        del profile['nodata']
        
profile.update(
   dtype='uint8'
    )

with rasterio.open(filepath_tif, 'w', **profile) as dst:
     dst.write(arr_rescaled,indexes=1)
     dst.update_tags(Percentile_1= percentile_1)
     dst.update_tags(SCALE_X1=scaleX1)
     dst.update_tags(SCALE_X2=scaleX2)

print("...Rescaling performed.\n")

# Convert GTiff to JPEG
cmd = ['gdal_translate', '-of', 'JPEG', '-co', 'worldfile=yes', filepath_tif,filepath_jpg]
sp.check_call(cmd, shell=True)

# Remove rescaled GTiff
os.remove(filepath_tif)

# Close input raster
src.close()

print("\nConversion of %s completed :-D"%filepath)
