# this is a Simple weather app using Open Weather API with python 
# You can give locations and based on the location get Weather Details 

# import nessasary libraries 

import requests

API_KEY= '2c3bbb89ceb06e4387cf31715e580892'



def runApp() :
    # get Location From the user 
    city = input(str("Enter Your City : "))
    GEO_LOCATION_URL= f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}'

    # get the location Details 
    location = getGeoLoaction(GEO_LOCATION_URL)
    # print(location)

    # get the Weather Details 
    lat = location['lat']
    lon = location['lon']

    WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    print(WEATHER_URL)
    weatherJson = getWeather(WEATHER_URL)
    weather = weatherJson['weather'][0]['description']

    printString(city,weather)
    


def getGeoLoaction(url) :
    resposne = requests.get(url).json()
    cordinates = {"lat" : resposne[0]['lat'] , "lon" : resposne[0]['lon']}
    print(cordinates)
    return cordinates
   

def getWeather (url) :
    response = requests.get(url).json()
    # print(response) 
    return response

def printString(city:str, weather:str):
    print (f'Weather in {city} is {weather}')

# main function 
if __name__ == "__main__":
    runApp()
