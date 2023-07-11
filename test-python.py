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
url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&exclude=hourly,daily&cnt=2&lang=pt&units=metric&appid={API_KEY}'

response = requests.get(url)

print(response.json())

# r+ is for both reading and writing
with open('weather-output.json', 'r+') as f:
    try: 
        existing_data = json.load(f)     #  load   [1, 2, 3]  from the file
        existing_data.extend([4, 5, 6])  #  add    [4, 5, 6]   to the loaded data
        json.dump(f, existing_data)     #   write  [1, 2, 3, 4, 5, 6]  to the file
    except: 
        json.dump(f,[4, 5, 6])
