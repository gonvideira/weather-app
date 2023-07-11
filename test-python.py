import requests
import os

try:
    API_KEY = os.environ['WEATHER_MAP_API']
except KeyError:
    API_KEY = 'Token not available!'
    print(API_KEY)
    # or raise an error if it's not available so that the workflow fails

# response = requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&appid='+API_KEY+'&lang=pt')
response = requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&appid=' + API_KEY)
# response = requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99')

print('Hello World!')
print(response.json())