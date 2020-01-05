
import json
from pathlib import Path

project_dir = str(Path(__file__).resolve().parents[1])
print(f"running: {__file__}")






# first, load census block code map for illinois
file_path = project_dir + "/data/interem/" + "tl_2018_17_tabblock10.geojson"
assert file_path ==  "/Users/erik/broadband_access_research/broadband-map-experiment/data/interem/tl_2018_17_tabblock10.geojson", "check file path"
with open(file_path) as json_file:
    map_il = json.load(json_file)
print('tl_2018_17_tabblock10.geojson loaded as map_il')

print('map_il has {} features'.format(len(map_il['features'])))

# make skeleton of map_cook_county dictionary
map_cook_county = {
"type": "FeatureCollection",
"name": "tl_2018_17_tabblock10",
"features": []
}

# add only cook county (code '031') to map_cook_county
for feature in map_il['features']:
    county_code = feature['properties']['COUNTYFP10']
    if county_code == '031':
        map_cook_county['features'].append(feature)
print("features for cook county copied to map_cook_county")
print('map_cook_county has {} features'.format(len(map_cook_county['features'])))

# write to json
file_path = project_dir + "/data/interem/" + "cook_county_map_data.geojson"
assert file_path == "/Users/erik/broadband_access_research/broadband-map-experiment/data/interem/cook_county_map_data.geojson", "check file path"
with open(file_path, 'w') as outfile:
    json.dump(map_cook_county, outfile, indent = 2)
print("writing map_il to cook_county_map_data.geojson done")