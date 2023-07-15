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

def write_json(new_data, filename='weather-output.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details / I took ['empl_data'] out.. may have to add if error
        file_data.append(new_data[0])
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 6)
        file.close()

def retrieve_data():
    # url to fecth new data
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&exclude=hourly,daily&cnt=2&lang=pt&units=metric&appid={API_KEY}'
    response = requests.get(url)
    new_data = response.json()['list']
    # print response and data
    print(response.json()['cod'])
    print(new_data)
    # call write_json function to append new data to file
    write_json(new_data)

# will eventually need to check if duplicates were appended

if __name__ == "__main__":
    retrieve_data()
