
# What is pandas-python? Introduction and Installation








# now we will see in pandas 

import pandas as pd
df = pd.read_csv('nyc_weather.csv')
df
#get the maximum temparature 
df['Temperature'].max()
#to know which day it rains
df['EST'][df['Events'] == 'Rain']
#3. average wind speed
df['WindSpeedMPH'].mean()

# Installation


