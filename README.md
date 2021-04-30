# Introduction
This work has been carried out in the framework of [TWIGA](https://twiga-h2020.eu/), a project funded from the European Union's Horizon 2020 research and innovation program (grant agreement No 776691).

TWIGA aims at providing currently unavailable geo-information to improve weather forecasting and water resources management in sub-Saharan Africa. The DEIB and DICA research groups of Politecnico di Milano are involved in the TWIGA activities related to the generation of highly accurate, dense, and wide water vapor maps to be supplied to local meteorological services to be ingested by NWP models and improve the prediction of heavy rainfall.

The main drawback in trasmitting water vapor products is certainly related to the size of the GeoTIFF ZTD maps, which can reach the order of hundreds of MegaBytes per map. This problem has been overcome by implementing a compression method that converts GeoTIFFs to georeferenced JPEGs.


# Script execution

1. Environment configuration
2. GeoTIFF to JPEG conversion
3. GeoTIFF recovering from JPEG

## Environment configuration
The code is entirely based on Python libraries (python-gdal, rasterio, numpy, scipy, etc.). 
