# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:32:34 2021

@author: Molinari
"""

import os,sys
import subprocess as sp
from PIL import Image
import numpy as np
import rasterio
import argparse


parser = argparse.ArgumentParser(description='GeoTIFF recovery from JPEG')
parser.add_argument('input', type=str,
                   help='JPEG image')


# Functions
def GetPar(lst,name):
    matchers = [name]
    matching = [s for s in lst if any(xs in s for xs in matchers)]
    return float((matching[0].split(">")[1]).split("<")[0])

# Get input argument
args = parser.parse_args()
filepath_jpg = args.input

# Define temporary and output files
filepath_tiff = filepath_jpg.split(".")[0] + "_1.tif"
filepath_Gtiff = filepath_jpg.split(".")[0] + ".tif"

# Check if all the encessary files exist

if not os.path.isfile(filepath_jpg +".aux.xml"):
    print("\n%s input file not available. The conversion cannot be executed.\n"%(filepath_jpg +".aux.xml"))
    sys.exit()
    
if not os.path.isfile(filepath_jpg.split("jpg")[0] +"wld"):
    print("\n%s input file not available. The conversion cannot be executed.\n"%(filepath_jpg.split("jpg")[0] +"wld"))
    sys.exit()
    
if not os.path.isfile(filepath_jpg.split(".jpg")[0] +"_mask.gif"):
    print("\n%s input file not available. The conversion cannot be executed.\n"%(filepath_jpg.split(".jpg")[0] +"_mask.gif"))
    sys.exit()

print("\nConversion of %s started...\n"%filepath_jpg)

# Convert jpeg to GeoTiff
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

# Open GeoTiff, rescale and add percentile_1
src = rasterio.open(filepath_tiff)
arr=src.read(1)
cols=arr.shape[1]
rows=arr.shape[0]

new_arr = arr * scaleX1 + scaleX2

if percentile_1<0:
    new_arr = new_arr + percentile_1
    
print("\n...Rescaling performed.\n")

# Read and apply mask
img = Image.open(filepath_jpg.split(".jpg")[0] +"_mask.gif")
mask_arr = np.asarray(img)
new_arr[mask_arr==0]=-9999
img.close()

print("...Masking performed.\n")

# Save rescaled GeoTiff
profile = src.profile.copy()
profile.update(
   dtype='float64',
   nodata=-9999,
   compress='packbits'
    )

with rasterio.open(filepath_Gtiff, 'w', **profile) as dst:
     dst.write(new_arr,indexes=1)

src.close()  

# Remove not rescaled GeoTiff
os.remove(filepath_tiff)
          
print("Conversion of %s completed :-D\n"%filepath_jpg)

