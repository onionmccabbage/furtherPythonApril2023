import numpy as np
import pandas as pd

town_list = ['Cork', 'Dublin', 'Galway', 'Athlone', 'Shannon', 'Roscarberry']
year_list = [2017, 2018, 2019, 2020, 2021, 2022] # a list
pop_list  = [1.5, 1.7, 3.6, 2.4, 2.9, 3.2] # a list
data = {'town':town_list, 'year':year_list, 'pop': pop_list } # a dict

df = pd.DataFrame(data)

print(df)