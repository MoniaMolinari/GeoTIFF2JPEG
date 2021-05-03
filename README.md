# Introduction
This work has been carried out in the framework of [TWIGA](https://twiga-h2020.eu/), a project funded from the European Union's Horizon 2020 research and innovation program (grant agreement No 776691).

TWIGA aims at providing currently unavailable geo-information to improve weather forecasting and water resources management in sub-Saharan Africa. The DEIB and DICA research groups of Politecnico di Milano are involved in the TWIGA activities related to the generation of highly accurate, dense, and wide water vapor maps to be supplied to local meteorological services to be ingested by NWP models and improve the prediction of heavy rainfall.

The main drawback in data delivery and storage of water vapor products is certainly related to their size, which can reach the order of hundreds of MegaBytes per map. This problem has been overcome by implementing a compression method able to drastically reduce file size without significant accuracy losses.

The repository provides the Python scripts implementing the compression/decompression method and a water vapor product for testing. In the following, instructions about the environment configuration and the scripts execution are provided.

# Dataset
An example of water vapor map in GeoTIFF format can be dowloaded from [here](//www.dropbox.com/s/1so24p6d0tw76m2/20180402163741_APS_MM_ZENITH_MERGED.tif?dl=0). The map is related to South Africa areas and is derived from the synergic use of SAR Sentinel-1 and GNSS data. The file size is about 170 MB.

# Script execution

1. Environment configuration
2. GeoTIFF to JPEG conversion
3. GeoTIFF recovery from JPEG

## Environment configuration
The code is entirely based on Python 3.7 and Python libraries ([GDAL Python](https://gdal.org/api/python.html), [rasterio](https://rasterio.readthedocs.io/en/latest/), [numpy](https://numpy.org/), [scipy](https://www.scipy.org/), [PIL](https://pillow.readthedocs.io/en/stable/), [subprocess](https://docs.python.org/3/library/subprocess.html)). 

## GeoTIFF to JPEG conversion

## GeoTIFF recovery from JPEG
