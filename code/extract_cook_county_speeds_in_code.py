import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parents[2]


# import in pieces
# for each piece, ask if county is cook
# cook county code is ...
# search for census code at 60660 yeilds:
# 170310306012004
# okay. the 17031 stands for IL (17) and Cook County (031)
# if it is, save all columns to fcc DataFrame


# set up data import
# file_path = "Users/erik/broadband_access_research/broadband-map/data/Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv"
# file_path = "fake.csv"
# chunk_size = 10**6
# text_file_reader = pd.read_csv(file_path, chunksize=chunk_size)
file_path_2 = str(project_dir) + "/broadband-map-experiment/data/raw/Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv"
file_path = "/Users/erik/broadband_access_research/broadband-map-experiment/data/raw/Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv"
chunk_size=10**6
text_file_reader = pd.read_csv(file_path_2, chunksize=chunk_size)
print("opening file")

# shoul be be approx 69 chunks

# import data
fcc = pd.DataFrame()
for i, chunk in enumerate(text_file_reader):
    if i < 10:
        i+= 1
        continue
    if i ==11:
        break
    print()
    print(f"importing chunk {i}")
    print(chunk)
    select = chunk[chunk["Census Block FIPS Code"]//(10**10) == 17031]  # cook county
    print("Selected records")
    print(select)
    fcc = fcc.append(select)

print("saving file")
fcc.to_csv('data' /' my_fcc.csv')
