import requests
import os

try:
    API_KEY = os.environ['WEATHER_MAP_API']
except KeyError:
    API_KEY = 'Token not available!'
    print(API_KEY)
    # or raise an error if it's not available so that the workflow fails

lat = 38.60492907958181
lon = -9.211457576882433
url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&exclude=hourly,daily&appid={API_KEY}'

response = requests.get(url)

print(response.json())
