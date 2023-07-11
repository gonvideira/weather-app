import requests
import certifi
import os

try:
    API_KEY = os.environ['WEATHER_MAP_API']
except KeyError:
    API_KEY = 'Token not available!'
    print(API_KEY)
    # or raise an error if it's not available so that the workflow fails

try:
  print('Checking connection to Github...')
  response_Git = requests.get('https://api.github.com')
  print('Connection to Github OK.')
except requests.exceptions.SSLError as err:
  print('SSL Error. Adding custom certs to Certifi store...')
  cafile = certifi.where()
  with open('certicate.pem', 'rb') as infile:
    customca = infile.read()
  with open(cafile, 'ab') as outfile:
    outfile.write(customca)
    print('That might have worked.')

url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID='+API_KEY
# response = requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&appid='+API_KEY+'&lang=pt')
# response = requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99')
response = requests.get(url)

print('Hello World!')
print(response_Git.json())
print(response.json())
