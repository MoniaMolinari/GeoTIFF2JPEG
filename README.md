# Introduction
This work has been carried out in the framework of [TWIGA](https://twiga-h2020.eu/), a project funded from the European Union's Horizon 2020 research and innovation program (grant agreement No 776691).

TWIGA aims at providing currently unavailable geo-information to improve weather forecasting and water resources management in sub-Saharan Africa. The DEIB and DICA research groups of Politecnico di Milano are involved in the TWIGA activities related to the generation of highly accurate, dense, and wide water vapor maps to be supplied to local meteorological services to be ingested by NWP models and improve the prediction of heavy rainfall.

The main drawback in data delivery and storage of water vapor products is certainly related to their size, which can reach the order of hundreds of MegaBytes per map. This problem has been overcome by implementing a compression method able to drastically reduce file size without significant accuracy losses.

The repository provides the Python scripts implementing the compression/decompression method and a water vapor product for testing. In the following, instructions about the environment configuration and the scripts execution are provided.

# Dataset
An example of water vapor map in GeoTIFF format can be dowloaded from [here](https://www.dropbox.com/s/k92yz0zgyn7pal5/abs20180321.tif?dl=0). The map is related to South Africa areas and is derived from the synergic use of SAR Sentinel-1 and GNSS data. The file size is about 170 MB.

![alt text](https://www.dropbox.com/s/oy441nbadm4ckew/ZTD_assoluta.png?dl=0)

# Script execution

1. Environment configuration
2. GeoTIFF to JPEG conversion
3. GeoTIFF recovering from JPEG

## Environment configuration
The code is entirely based on Python libraries (python-gdal, rasterio, numpy, scipy, etc.). 
