from threading import Thread
import json
import requests
import time

from weatherService import TempGetter

# CITIES = [
#     'Athlone', 'Dublin', 'Galway', 'Belfast', 
#     'London', 'Cork', 'Lund', 'Kista'
# ]
# CITIES = [
#     'Athlone', 'Canberra', 'London', 'Athens'
# ]
from memory_profiler import profile

@profile
def main():
    # maybe try using a generator for these cities (improve performance)
    CITIES = ["Dublin","Cork","Limerick","Galway","Waterford","Drogheda","Kilkenny","Wexford","Sligo","Clonmel","Dundalk","Bray","Ennis","Tralee","Carlow","Naas","Athlone","Letterkenny","Tullamore","Killarney","Arklow","Cobh","Castlebar","Midleton","Mallow","Ballina","Enniscorthy","Wicklow","Cavan","Athy","Longford","Dungarvan","Nenagh","Trim","Thurles","Youghal","Monaghan","Buncrana","Ballinasloe","Fermoy","Westport","Carrick-on-Suir","Birr","Tipperary","Carrickmacross","Kinsale","Listowel","Clonakilty","Cashel","Macroom","Castleblayney","Kilrush","Skibbereen","Bundoran","Templemore","Clones","Newbridge","Mullingar","Balbriggan","Greystones","Leixlip","Tramore","Shannon","Gorey","Tuam","Edenderry","Bandon","Loughrea","Ardee","Mountmellick","Bantry","Boyle","Ballyshannon","Cootehill","Ballybay","Belturbet","Lismore","Kilkee","Granard"]

    threads = [TempGetter(c) for c in CITIES]
    start = time.time()
    # first we kick off all the threads
    for thread in threads:
        thread.start()

    # now we wait for all the threads to complete
    for thread in threads:
        thread.join()
        print(
            "it is {0.temperature:.4f}°C in {0.city:s}".format(thread))

    print(
        "Got {} reports in {} seconds".format(len(threads), time.time() - start))

if __name__ == '__main__':
    main()
