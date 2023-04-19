from threading import Thread
from memory_profiler import profile
import requests
from timeit import default_timer

class TempGetter(Thread):
    def __init__(self, city):
        """
        The __init__ method initializes the TempGetter class
        Takes a 'city' parameter
        """
        super().__init__()
        self.city = city
        self.temperature = -99

    def run(self):
        """
        The run method is invoked when this class is the target of a thread
        """
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
        response = requests.get(url_template.format(self.city))
        data = response.json()
        self.temperature = data['main']['temp']

@profile
def getWeather(cities=['athlone', 'galway']):
    """
    the getWeather method takes a list of cities and returns the temperature for each city.

    """
    threads = [TempGetter(c) for c in cities]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for thread in threads:
        return (thread.temperature)

if __name__ == '__main__':
    s = default_timer()
    x = getWeather()
    print(x)
    e = default_timer()
    print(f'time: {e-s}')