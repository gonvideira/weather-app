import requests
import certifi
import os

try:
    API_KEY = os.environ['WEATHER_MAP_API']
except KeyError:
    API_KEY = 'Token not available!'
    print(API_KEY)
    # or raise an error if it's not available so that the workflow fails

# url = 'http://api.openweathermap.org/data/2.5/weather?q=Caparica,pt&APPID=' + API_KEY
lat = 38.60492907958181
lon = -9.211457576882433
url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&exclude=hourly,daily&appid={API_KEY}'
# response = requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&appid='+API_KEY+'&lang=pt')
response = requests.get(url)

print('Hello World!')

print(response.json())
