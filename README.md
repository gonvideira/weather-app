# weather-app
To work and develop my weather app project. 

## Task List
- [x] Add a worflow to install Python
- [x] Add requirements file to pip install
- [x] Add a python file with basic testing
- [x] Add the basic python file to the workflow testing
- [ ] Find public API to work with
- [ ] Work on a more complicated python file and try to commit changes to a local file in the repo

> Check the [Python engineer page](https://www.python-engineer.com/posts/run-python-github-actions/)  
> Public weather API: [Open Weather Maps API](https://openweathermap.org/api/one-call-3#how) and [Open Weather Maps - Caparica](https://openweathermap.org/city/8013114) and [AccuWeather](https://developer.accuweather.com/packages)

```
Generic API calls: 
https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API key}
http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

Examples: 
https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&appid={API key} # example of city
https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=38.603504185497236&lon=-9.211465596431635&appid={API key} # Caparica

```
