"""
Python file for retrieving weather data.

This file is hard wired to Costa da Caparica. 
"""
import json
from datetime import datetime as dt
from datetime import timezone as tz
import pytz
import os
import requests

# Constant variables
API_KEY = os.environ['WEATHER_MAP_API']
LAT = 38.60492907958181
LON = -9.211457576882433
COUNT = 20
NOW = dt.now(tz.utc)
FN = 'output/weather-output.json'

print(f'Time now is {NOW}')

def remove_duplicate_items(_api_data, _key):
    """function to check if duplicates were appended and delete the initial ones"""
    print(f"Initial items in list: {len(_api_data)}")
    unique_elements = []
    cleaned_data = []
    keys = []
    for i,j in enumerate(_api_data):
        date_api_format = dt.strptime(_api_data[i]['dt_txt'], '%Y-%m-%d %H:%M:%S')
        date_api = date_api_format.replace(tzinfo=pytz.utc)
        if _api_data[i][_key] not in unique_elements and date_api >= NOW:
            unique_elements.append(_api_data[i][_key])
            keys.append(i)
    for key in reversed(keys):
        cleaned_data.append(_api_data[key])
    print(
        f"Total duplicates removed: {len(_api_data) - len(unique_elements)}, Total items: {len(_api_data)}, Final items:{len(unique_elements)}")
    print(f"Final items in list: {len(cleaned_data)}")
    # Sort the JSON data based on the value of the brand key
    cleaned_data.sort(key=lambda x: x['dt_txt'])
    print(f'The sorted JSON data based on the value of the date:\n{cleaned_data}')
    return cleaned_data

def write_json(new_data, filename=FN):
    """function to write new data in existing json file"""
    with open(filename,'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data
        for data in new_data:
            file_data.append(data)
        # delete duplicates
        new_data = remove_duplicate_items(file_data, 'dt')
        # Sets file's current position at offset.
        file.seek(0)
        file.close()

    print(f'Overwriting {filename}')
    with open(filename, "wt") as file:
        json.dump(new_data, file, indent = 6)
        file.close()

def retrieve_data():
    """function that retrieves original data from API"""
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&exclude=hourly,daily&cnt={COUNT}&lang=pt&units=metric&appid={API_KEY}'
    response = requests.get(url)
    new_data = response.json()['list']
    # call write_json function to append new data to file
    write_json(new_data)

if __name__ == "__main__":
    retrieve_data()
