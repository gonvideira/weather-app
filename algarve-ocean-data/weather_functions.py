"""Functions to retrieve and treat weather data"""
import os
import json
from datetime import datetime as dt
from datetime import timezone as tz
import pytz
import requests
import pandas as pd

FOLDER = 'algarve-ocean-data/'
NOW = dt.now(tz.utc)

def remove_duplicate_items(_api_data, _key):
    """function to check if duplicates were appended and delete the initial ones"""
    print(f"Initial items in list: {len(_api_data)}")
    unique_elements = []
    cleaned_data = []
    keys = []
    for i,j in enumerate(_api_data):
        date_api_format = dt.strptime(_api_data[i]['SDATA'], '%Y-%m-%d %H:%M')
        date_api = date_api_format.replace(tzinfo=pytz.utc)
        if _api_data[i][_key] not in unique_elements and date_api < NOW:
            unique_elements.append(_api_data[i][_key])
            keys.append(i)
    for key in reversed(keys):
        cleaned_data.append(_api_data[key])
    print(
        f"Total duplicates removed: {len(_api_data) - len(unique_elements)}, Total items: {len(_api_data)}, Final items:{len(unique_elements)}")
    print(f"Final items in list: {len(cleaned_data)}!\n")
    # Sort the JSON data based on the value of the brand key
    cleaned_data.sort(key=lambda x: x['SDATA'])
    # print(f'The sorted JSON data based on the value of the date:\n{cleaned_data}')
    return cleaned_data

def write_json(new_data, filename):
    """function to write new data in existing json file"""

    with open(filename,'r',encoding='utf-8') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data
        for data in new_data:
            file_data.append(data)
        # delete duplicates
        new_data = remove_duplicate_items(file_data, 'SDATA')
        # Sets file's current position at offset.
        file.seek(0)
        file.close()
    
    print(f'Overwriting {filename}...')
    with open(filename, "wt",encoding='utf-8') as file:
        json.dump(new_data, file, indent = 6)
        file.close()
        print(f'File {filename} populated with new data.\n')

def retrieve_data(url_map):
    """function that retrieves original data from IH"""
    
    for key, value in url_map.items():
        print(f"KEY: -{key}-\n")
        print(f"URL: -{value}-\n")
        response = requests.get(value, timeout=10)
        decoded_data=response.text.encode().decode('utf-8-sig')
        new_data = json.loads(decoded_data)
        print(f"Data -{key}- retrieved!\n")
        print(f"Data here:\n{new_data}\n")
        # call write_json function to append new data to file
        file_name = FOLDER + f"/weather-data-{key}.json"
        csv_name = FOLDER + f"/weather-data-{key}.csv"
        write_json(new_data, file_name)
        delete_files(csv_name)
        create_csv(file_name, csv_name)

    return print("All done!\n")

def delete_files(csv_name):
    """delete detailed"""
    try:
        os.remove(csv_name)
    except FileNotFoundError:
        print('CSV file not present!\n')

    return print('Folder clean!\n')

def create_csv(json_file, csv_name):
    """create a CSV from the updated json file"""
    df = pd.read_json(json_file,encoding='utf-8')
    df.to_csv(csv_name,encoding='utf-8',index=False)
    return print('CSV file created!\n')
