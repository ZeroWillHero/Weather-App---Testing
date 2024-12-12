from main import getGeoLoaction, getWeather, printString

API_KEY='2c3bbb89ceb06e4387cf31715e580892'

def test_getGeoLoaction():
    city = 'London'
    GEO_LOCATION_URL= f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}'

    # test case 1
    expect = {'lat': 51.5073219, 'lon': -0.1276474}
    assert getGeoLoaction(GEO_LOCATION_URL) == expect



def test_printString(capfd):
    city = "New York"
    weather = "sunny"
    printString(city, weather)
    captured = capfd.readouterr()
    assert captured.out == "Weather in New York is sunny\n"

    # test Case 2
    city = "Tokyo"
    weather = "sunny"
    printString(city, weather)
    captured = capfd.readouterr()
    assert captured.out == "Weather in Tokyo is sunny\n"


    # test Case 3
    city = "London"
    weather = "sunny"
    printString(city, weather)
    captured = capfd.readouterr()
    assert captured.out == "Weather in London is sunny\n"