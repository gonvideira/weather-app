import requests
import os
import json

try:
    API_KEY = os.environ['WEATHER_MAP_API']
except KeyError:
    API_KEY = 'Token not available!'
    print(API_KEY)
    # or raise an error if it's not available so that the workflow fails

lat = 38.60492907958181
lon = -9.211457576882433

# function to check if duplicates were appended and delete the initial ones
def remove_duplicate_items(_api_data, _key):
    print("Initial items in list: {}".format(len(_api_data)))
    unique_elements = []
    cleaned_data = []
    keys = []
    for i, j in enumerate(_api_data):
        if _api_data[i][_key] not in unique_elements:
            unique_elements.append(_api_data[i][_key])
            keys.append(i)

    for key in reverse(keys):
        cleaned_data.append(_api_data[key])

    print(
        "Total duplicates removed: {}, Total items: {}, Final items:{}".format(
            (len(_api_data) - len(unique_elements)),
            len(_api_data), len(unique_elements)))
    print("Final items in list: {}".format(len(cleaned_data)))

    return cleaned_data

# functtion to write new data in existing json file
def write_json(new_data, filename='weather-output.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details / I took ['empl_data'] out.. may have to add if error
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # delete duplicates
        unique_data = remove_duplicate_items(file_data, "dt")
        # convert back to json.
        json.dump(unique_data, file, indent = 6)
        file.close()

def retrieve_data():
    # url to fecth new data
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&exclude=hourly,daily&cnt=2&lang=pt&units=metric&appid={API_KEY}'
    response = requests.get(url)
    new_data = response.json()['list']
    # print response and data
    print(response.json()['cod'])
    print(new_data[0])
    # call write_json function to append new data to file
    write_json(new_data[0])


if __name__ == "__main__":
    retrieve_data()
