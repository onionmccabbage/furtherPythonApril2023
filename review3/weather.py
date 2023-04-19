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
    CITIES = ["Dublin","Cork","Limerick","Galway","Waterford","Drogheda","Kilkenny","Wexford","Sligo","Clonmel","Dundalk","Bray","Ennis","Tralee","Carlow","Naas","Athlone","Letterkenny","Tullamore","Killarney","Arklow","Cobh","Castlebar","Midleton","Mallow","Ballina","Enniscorthy","Wicklow","Cavan","Athy","Longford","Dungarvan","Nenagh","Trim","Thurles","Youghal","Monaghan","Buncrana","Ballinasloe","Fermoy","Westport","Carrick-on-Suir","Birr","Tipperary","Carrickmacross","Kinsale","Listowel","Clonakilty","Cashel","Macroom","Castleblayney","Kilrush","Skibbereen","Bundoran","Templemore","Clones","Newbridge","Mullingar","Balbriggan","Greystones","Leixlip","Tramore","Shannon","Gorey","Tuam","Edenderry","Bandon","Loughrea","Ardee","Mountmellick","Bantry","Boyle","Ballyshannon","Cootehill","Ballybay","Belturbet","Lismore","Kilkee","Granard"]
    x = getWeather(CITIES)
    print(x)
    e = default_timer()
    print(f'time: {e-s}')