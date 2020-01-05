import pandas as pd
from pathlib import Path

PROJECT_DIR = str(Path(__file__).resolve().parents[1])
print(f"running: {__file__}")


def load_cook_county():
    # First, load the cook county fcc data from interim data
    file_path = PROJECT_DIR + "/data/interim/" + "cook_county_fcc.csv"
    print()
    df = pd.read_csv(file_path)
    return df


def select_consumer(df):
    df = df[['Consumer', 'Max Advertised Downstream Speed (mbps)', 'Census Block FIPS Code', 'Max Advertised Upstream Speed (mbps)' ]]
    df = df[df['Consumer'] == 1]
    groups = df.groupby('Census Block FIPS Code')
    max_speed_by_block_code = groups['Max Advertised Downstream Speed (mbps)'].max()
    return max_speed_by_block_code


def save_max_speeds(max_speed_by_block_code):
    file_path = PROJECT_DIR + "/data/interim/" + "max_speed_by_block_code.csv"
    max_speed_by_block_code.to_csv(file_path, header=True)


def main():
    file_path = PROJECT_DIR + "/data/interim/" + "cook_county_fcc.csv"
    assert file_path == "/Users/erik/Desktop/broadband-map-experiment/data/interim/cook_county_fcc.csv"
        # edit for your local machine
    df = load_cook_county()
    max_speed_by_block_code = select_consumer(df)
    assert max_speed_by_block_code.iloc[5] == 987.0, "Failed test based on what the data looked like on initial run"
    save_max_speeds(max_speed_by_block_code)