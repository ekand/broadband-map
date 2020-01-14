Broadband Access Research Map Project

Reproducing the Python environment:
Use the included spec-file.txt and follow the instructions here: 
[https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments).  It will probably help to install anaconda first.

DATA
Internet speed data comes from the FCC. The website where I downloaded the csv file is [https://opendata.fcc.gov/Wireline/Fixed-Broadband-Deployment-Data-Jun-2018-Status-V1/ehbi-rr4z](https://opendata.fcc.gov/Wireline/Fixed-Broadband-Deployment-Data-Jun-2018-Status-V1/ehbi-rr4z).

Cook county census block code mapping data comes from the US Census Bureau.
I downloaded the shapefiles from here: [https://www.census.gov/cgi-bin/geo/shapefiles/index.php](https://www.census.gov/cgi-bin/geo/shapefiles/index.php), then used ogr2ogr to convert them from the Census Bureau's format to the more widely used .geojson format. Details in /data/data_collection_notes.txt


The steps to process the files are summarized in   
Code to process files:
extract_cook_county_speeds.py




The project structure is:
```
broadband-map-experiment
.  
├── LICENSE  
├── README.md
├── code
│   └── extract_cook_county_speeds_in_code.py
└── data
    ├── interem
    │   ├── cook_county_fcc.csv
    │   └── head_of_cook_county_fcc.csv
    ├── processed
    └── raw
        ├── Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv
        └── head_of_Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.txt
```

Point of interest: /data/raw/tl_2018_17_tabblock10 has census blocks for all of illinois but I only want cook county.


# Data Processing  
First there's /code/get_cook_county_block_code_map.py. This file loads the fcc data from /data/raw/Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv , and extracts the part of it which is cook county. It then saves this data to 


# Accessing scripts in /code/ from jupyter notebooks in /code/
After installing a pipenv environment and activating the shell, I ran the following:  
`pipenv install -e .`  
This installs all packages in the working directory (which was broadband-map-experiment). In this case the only package is called code
