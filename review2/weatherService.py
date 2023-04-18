from threading import Thread
import json
import requests
import time

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
        response = requests.get(url_template.format(self.city))
        data = json.loads(response.text)
        self.temperature = data['main']['temp']
        # lon = 0
        # lat = 52
        # r = requests.get('https://www.google.co.uk/maps/place/{},{}'.format(lon, lat))
        # print(r.text)