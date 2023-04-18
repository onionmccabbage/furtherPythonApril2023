from threading import Thread
import threading
import json
import requests
import time

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city
        self.__lock = threading.Lock()
        self.__weatherStructure = []
        self.__count = 0

    def run(self):
        self.__lock.acquire()
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
        try:
            response = requests.get(url_template.format(self.city))
            data = json.loads(response.text)
            self.description = data['weather'][0]['description']
            self.temperature = data['main']['temp']
            self.windSpeed = data['wind']['speed']
            self.windDirection = data['wind']['deg']
            self.lat = data['coord']['lat']
            self.lon = data['coord']['lon']
        except Exception as e:
            print(e)
        # persist the weather data in a global structure
        self.__weatherStructure.append({
            'city':self.city,
            'description':self.description,
            'temperature':self.temperature,
            'wind':{'speed':self.windSpeed, 'direction':self.windDirection},
            'lat':self.lat, 
            'lon':self.lon})
        self.__count += 1
        # fetch a geographic map
        url = 'https://www.google.co.uk/maps/place/{},{}'.format(self.lat, self.lon)
        # print(url)
        r = requests.get(url)
        fout = open('map.html', 'wt', encoding="utf-8")
        try:
            print(r.text, file=fout)
        except Exception as e:
            print(e)

        # release the lock
        self.__lock.release()