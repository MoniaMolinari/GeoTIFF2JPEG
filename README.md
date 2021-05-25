# Introduction
This work has been carried out in the framework of [TWIGA](https://twiga-h2020.eu/), a project funded from the European Union's Horizon 2020 research and innovation program (grant agreement No 776691).

TWIGA aims at providing currently unavailable geo-information to improve weather forecasting and water resources management in sub-Saharan Africa. The DEIB and DICA research groups of Politecnico di Milano are involved in the TWIGA activities related to the generation of highly accurate, dense, and wide water vapor maps to be supplied to local meteorological services to be ingested by NWP models and improve the prediction of heavy rainfall.

The main drawback in data delivery and storage of water vapor products is certainly related to their size, which can reach the order of hundreds of MegaBytes per map. This problem has been overcome by implementing a compression method able to drastically reduce file size without significant accuracy losses.

The repository provides the Python scripts implementing the compression/decompression method and a water vapor product for testing. In the following, instructions about the environment configuration and the scripts execution are provided.

# Dataset
An example of water vapor map in GeoTIFF format can be dowloaded from [here](https://www.dropbox.com/s/0vf0s90gvnculq3/20180402163741_APS_MM_ZENITH.tif?dl=0). The map is related to South Africa areas and is derived from the synergic use of SAR Sentinel-1 and GNSS data. The file size is about 170 MB.

# Script execution

1. Environment configuration
2. GeoTIFF to JPEG conversion
3. GeoTIFF recovery from JPEG

## Environment configuration
The code is entirely based on Python 3.7 and Python libraries ([GDAL Python](https://gdal.org/api/python.html), [rasterio](https://rasterio.readthedocs.io/en/latest/), [numpy](https://numpy.org/), [scipy](https://www.scipy.org/), [PIL](https://pillow.readthedocs.io/en/stable/)). 

The installation of [Anaconda toolkit](https://www.anaconda.com/products/individual) is suggested as it provides all necessary tools in one package.
In the repository *SCRIPTS* folder the [*geo.yml*](SCRIPTS/geo.yml) file is provided to setup the working environment. Download the *.yml* file, then open the Anaconda Prompt:
- Create the virtual environment (called *geo*) by typing:
```
conda env create -f /path_to_yml/geo.yml
```
- Activate the new environment by typing:
```
conda activate geo
```

## GeoTIFF to JPEG conversion
The script requires as input the path to the GeoTIFF image to convert in JPEG format. From the Anaconda Prompt type:
```
python /path_to_script/GTiff2jpg.py /path_to_image/image.tif
```
The output consists of the image in JPEG format and three auxiliary files for rescaling (*.xml*), georeferencing (*.wld*) and masking (*.gif*) recover processes. The output files obtained by applying the GeoTiff2jpg conversion tool to the water vapor map proposed as example are available [here](https://www.dropbox.com/s/hu5wca8bkh23jo7/20180402163741_APS_MM_ZENITH_MERGED_recovered.tif?dl=0).

## GeoTIFF recovery from JPEG
The script requires as input the path to the JPEG image to recover in GeoTIFF format. The same folder must contains auxiliary files (*.gif*, *.xml* and *.wld*).
From the Anaconda Prompt type:
```
python /path_to_script/jpg2GTiff.py /path_to_image/image.jpeg
```
The output is the image recovered in GeoTIFF format. For the considered example the output image is available [here](https://www.dropbox.com/s/gjbiekl21sldcy7/20180402163741_APS_MM_ZENITH_MERGED_recovered.tif?dl=0).

# References
Molinari M.E, Manzoni M., Petrushevsky N., Monti-Guarnieri A., Venuti G., Meroni A.N., Mascitelli A., Parodi A. A novel procedure for generation of SAR-derived ZTD maps for
weather prediction: application to South Africa use case. nt. Arch. Photogramm. Remote Sens. Spatial Inf. Sci., 2021. 
