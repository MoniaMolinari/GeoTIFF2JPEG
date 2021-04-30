# Introduction
This work has been carried out in the framework of [TWIGA](https://twiga-h2020.eu/), a project funded from the European Union's Horizon 2020 research and innovation program (grant agreement No 776691).

TWIGA aims at providing currently unavailable geo-information to improve weather forecasting and water resources management in sub-Saharan Africa. The DEIB and DICA research groups of Politecnico di Milano are involved in the TWIGA activities related to the generation of highly accurate, dense, and wide water vapor maps to be supplied to local meteorological services to be ingested by NWP models and improve the prediction of heavy rainfall.

An example of water vapor map of South Africa derived from the synergic use of SAR and GNSS data is stored in DATA folder. The main drawback in data delivery and storage of water vapor products is certainly related to the size of the GeoTIFF maps, which can reach the order of hundreds of MegaBytes per map. This problem has been overcome by implementing a compression method able to drastically reduce file size without significant accuracy losses.


# Script execution

1. Environment configuration
2. GeoTIFF to JPEG conversion
3. GeoTIFF recovering from JPEG

## Environment configuration
The code is entirely based on Python libraries (python-gdal, rasterio, numpy, scipy, etc.). 
