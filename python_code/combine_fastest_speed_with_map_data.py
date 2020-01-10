import pandas as pd
from pathlib import Path
import json
import numpy as np


PROJECT_DIR = str(Path(__file__).resolve().parents[1])



def load_max_speeds():
    # first, load fastest speed by census block code
    file_path = PROJECT_DIR + "/data/interim/" + "max_speed_by_block_code.csv"
    assert file_path == "/Users/erik/broadband_access_research/broadband-map-experiment/data/interim" \
                        "/max_speed_by_block_code.csv", "check file path "
    speed_by_block = pd.read_csv(file_path)
    print("max_speed_by_block_code.csv loaded as speed_by_block")
    return speed_by_block


def load_cook_county_map():
    # next, load geojson data for cook county
    file_path = PROJECT_DIR + "/data/interim/" + "cook_county_map_data.geojson"
    assert file_path ==  "/Users/erik/broadband_access_research/broadband-map-experiment/data/interim" \
                         "/cook_county_map_data.geojson", "check file path "
    with open(file_path) as json_file:
        map_d = json.load(json_file)  # map_d for map dictionary
    print('tl_2018_17_tabblock10.geojson loaded as map_d')
    return map_d


def combine_map_and_speeds(map_d, speed_by_block):
    # insert 'top_speed' data into map_d
    for feature in map_d['features']:
        top_speed_mask = speed_by_block['Census Block FIPS Code'] == int(feature['properties']['GEOID10'])
        if not top_speed_mask.any():
            feature['properties']['top_speed'] = 0
    else:
        top_speed = speed_by_block[top_speed_mask].iloc[0, 1]
        # assert type(top_speed) == np.float64
        feature['properties']['top_speed'] = top_speed
    print("combining data complete")
    return map_d


def save_speed_map(map_d):
    # next, save the resulting map_d to a json
    file_path = PROJECT_DIR + "/data/processed/" + "cook_county_map_with_top_speeds.geojson"
    assert file_path == "/Users/erik/broadband_access_research/broadband-map-experiment/data/processed" \
                        "/cook_county_map_with_top_speeds.geojson", "check file path "
    with open(file_path, 'w') as outfile:
        json.dump(map_d, outfile)
    print("writing to cook_county_map_with_top_speeds.geojson done")


if __name__ == "__main__":
    print(f"running: {__file__}")