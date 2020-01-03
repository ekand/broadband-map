import pandas as pd
from pathlib import Path

project_dir = str(Path(__file__).resolve().parents[1])
print(f"running: {__file__}")

# First, load the cook county fcc data from interem data
file_path = project_dir + "/data/interem/" + "cook_county_fcc.csv"
# assert file_path == "/Users/erik/Desktop/broadband-map-experiment/data/interem/cook_county_fcc.csv"
df = pd.read_csv(file_path)

df = df[['Consumer', 'Max Advertised Downstream Speed (mbps)', 'Census Block FIPS Code', 'Max Advertised Upstream Speed (mbps)' ]]
df = df[df['Consumer'] == 1]
groups = df.groupby('Census Block FIPS Code')
max_speed_by_block_code = groups['Max Advertised Downstream Speed (mbps)'].max()
assert max_speed_by_block_code.iloc[5] == 987.0, "Failed test based on what the data looked like on initial run"


file_path = project_dir + "/data/interem/" + "max_speed_by_block_code.csv"
max_speed_by_block_code.to_csv(file_path, header=True)


