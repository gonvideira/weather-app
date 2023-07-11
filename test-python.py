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
    json.dump(f,json.dumps(response.json()))
