Broadband Access Research Map Project

DATA
Internet speed data comes from the FCC. The website where I downloaded the csv file is [https://opendata.fcc.gov/Wireline/Fixed-Broadband-Deployment-Data-Jun-2018-Status-V1/ehbi-rr4z](https://opendata.fcc.gov/Wireline/Fixed-Broadband-Deployment-Data-Jun-2018-Status-V1/ehbi-rr4z).

Cook county census block code mapping data comes from the US Census Bureau.
I downloaded the shapefiles from here: [https://www.census.gov/cgi-bin/geo/shapefiles/index.php](https://www.census.gov/cgi-bin/geo/shapefiles/index.php), then used ogr2ogr to convert them from the Census Bureau's format to the more widely used .geojson format. Details in /data/data_collection_log.txt



Code to process files:
extract_cook_county_speeds.py