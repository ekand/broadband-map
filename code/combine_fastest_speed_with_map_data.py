import pandas as pd
from pathlib import Path
import json

project_dir = str(Path(__file__).resolve().parents[1])
print(f"running: {__file__}")

# first, load fastest speed by census block code
file_path = project_dir + "/data/interem/" + "max_speed_by_block_code.csv"
speed_by_block = pd.read_csv(file_path)

# next, load geojson data for cook county

file_path = project_dir + "/data/interem/" + "tl_2018_17_tabblock10.geojson"
assert file_path == "/Users/erik/Desktop/broadband-map-experiment/data/interem/tl_2018_17_tabblock10.geojson"
with open(file_path) as json_file:
    map_d = json.load(json_file)
print('map_d loaded')

# insert 'top_speed' data into map_d
for feature in map_d['features']:
    if not (speed_by_block['Census Block FIPS Code'] == int(feature['properties']['GEOID10'])).any():
        feature['top_speed'] = 0 
    else:
        feature['top_speed'] = speed_by_block[ speed_by_block['Census Block FIPS Code'] == int(feature['properties']['GEOID10']) ]



# next, save the resulting map_d to a json
file_path = project_dir + "/data/processed/" + "tl_2018_17_tabblock10.geojson"
assert file_path == "/Users/erik/Desktop/broadband-map-experiment/data/processed/cook_county_top_speeds.geojson"
# with open (file_path, 



print('done')