from threading import Thread
import requests

class TempGetter(Thread):
    def __init__(self, city):
        """
        The __init__ method initializes the TempGetter class
        Takes a 'city' parameter
        """
        super().__init__()
        self.city = city
        self.temperature = -99

def getWeather(city='athlone'):
    url_template = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'
    print(url_template)
    response = requests.get(url_template.format(city))
    data = response.json()
    description = data['weather'][0]['description']
    temperature = data['main']['temp']
    wind_speed = data['wind']['speed']
    wind_deg = data['wind']['deg']
    return f'Weather in {city}: {description} {temperature}&deg; wind {wind_speed} from {wind_deg}&deg;'
