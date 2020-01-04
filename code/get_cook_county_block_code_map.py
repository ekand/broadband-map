
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


# remove non-cook county entries from the features list in map_il
features = map_il['features']
features_length_before = len(features)
for i, feature in enumerate(features):
    if feature['properties']['COUNTYFP10'] != "031":
        del features[i]
print('removed non-cook county entries from map_il')
features_length_after = len(features)
assert features_length_after < features_length_before, "features list should be shorter after removing non-cook-county entries"


# write to json
file_path = project_dir + "/data/interem/" + "cook_county_map_data.geojson"
assert file_path == "/Users/erik/broadband_access_research/broadband-map-experiment/data/interem/cook_county_map_data.geojson", "check file path"
with open(file_path, 'w') as outfile:
    json.dump(map_il, outfile, indent = 2)
print("writing map_il to cook_county_map_data.geojson done")