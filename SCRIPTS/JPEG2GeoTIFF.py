# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:32:34 2021

@author: Molinari
"""

import os,sys
import subprocess as sp
#from osgeo import gdal
from PIL import Image
import numpy as np
import rasterio

def GetPar(lst,name):
    matchers = [name]
    matching = [s for s in lst if any(xs in s for xs in matchers)]
    return float((matching[0].split(">")[1]).split("<")[0])

filepath_jpg=r"C:/Users/Molinari/Dropbox (DEIB)/MONIA/TWIGA/SUDAFRICA_2018/Diff_APS/20180402163741_APS_MM_ZENITH_MERGED.jpg"
filepath_tiff = filepath_jpg.split(".")[0] + "_1.tiff"
filepath_Gtiff = filepath_jpg.split(".")[0] + ".tiff"


if not os.path.isfile(filepath_jpg +".aux.xml"):
    sys.exit()
    
if not os.path.isfile(filepath_jpg.split("jpg")[0] +"wld"):
    sys.exit()
    
if not os.path.isfile(filepath_jpg.split(".jpg")[0] +"_mask.gif"):
    sys.exit()


# Convert to GeoTiff
cmd = ['gdal_translate', '-of', 'GTiff', filepath_jpg, filepath_tiff]
sp.check_call(cmd, shell=True)

#Read metadata for rescaling
f = open(filepath_jpg +".aux.xml", "r" )
a=[]
for line in f:
    a.append(line.strip())
f.close()
    
percentile_1 = GetPar(a,"Percentile_1")
scaleX1 = GetPar(a,"SCALE_X1")
scaleX2 = GetPar(a,"SCALE_X2")    

# Open GTiff, rescale and add percentile_1
src = rasterio.open(filepath_tiff)
arr=src.read(1)
cols=arr.shape[1]
rows=arr.shape[0]


new_arr = arr * scaleX1 + scaleX2

if percentile_1<0:
    new_arr = new_arr + percentile_1

# Read and apply mask
img = Image.open(filepath_jpg.split(".jpg")[0] +"_mask.gif")
mask_arr = np.asarray(img)
new_arr[mask_arr==0]=-9999
img.close()

# Remove jpg
os.remove(filepath_jpg)
os.remove(filepath_jpg +".aux.xml")
os.remove(filepath_jpg.split("jpg")[0] +"wld")
os.remove(filepath_jpg.split(".jpg")[0] +"_mask.gif")

# Save rescaled GTiff
profile = src.profile.copy()
profile.update(
   dtype='float64',
   nodata=-9999,
   compress='packbits'
    )

with rasterio.open(filepath_Gtiff, 'w', **profile) as dst:
     dst.write(new_arr,indexes=1)

src.close()     
os.remove(filepath_tiff)

