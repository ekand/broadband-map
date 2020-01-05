import pandas as pd
from pathlib import Path

PROJECT_DIR = str(Path(__file__).resolve().parents[1])

# import in pieces
# for each piece, ask if county is cook
# cook county code is ...
# search for census code at 60660 yields:
# 170310306012004
# okay. the 17031 stands for IL (17) and Cook County (031)
# if it is, save all columns to fcc DataFrame


def read_fcc_cook():
    # open file

    file_path = str(PROJECT_DIR) + "/data/raw/Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv"
    print(f'opening {file_path}')
    chunk_size = 10**6
    text_file_reader = pd.read_csv(file_path, chunksize=chunk_size)

    # import data, saving only cook county to the fcc DataFrame
    fcc_cook = pd.DataFrame()
    for i, chunk in enumerate(text_file_reader):
        # print()
        print(f"importing chunk {i} ", end='')
        # print(chunk)
        select = chunk[chunk["Census Block FIPS Code"]//(10**10) == 17031]  # cook county
        # print("Selected records")
        # print(select)
        fcc_cook = fcc_cook.append(select)
    print()
    return fcc_cook


def save_fcc_cook(fcc_cook):

    file_path = PROJECT_DIR + "/data/interim/cook_county_fcc.csv"
    print(f"saving {file_path}")
    fcc_cook.to_csv(file_path)


def main():
    """tests the functions in this module

    """
    print("running ", str(Path(__file__)))
    file_path = str(PROJECT_DIR) + "/data/raw/Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv"
    assert file_path == "/Users/erik/broadband_access_research/broadband-map-experiment/data/raw/Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv" # change for your local directory
    file_path = str(PROJECT_DIR) + "/data/raw/Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv"
    assert file_path == "/Users/erik/broadband_access_research/broadband-map-experiment/data/raw/Fixed_Broadband_Deployment_Data__Jun__2018_Status_V1.csv" # change for your local directory
    print("All tests passed. Have a nice day!")


if __name__ == '__main__':
    main()
