
# What is pandas-python? Introduction and Installation








# now we will see in pandas 
import pandas as pd
df = pd.read_csv("https://drive.google.com/file/d/1KxwFsL6IF7OD_XN28kjxl0-amnELIhZ8/view?usp=sharing")
df
from google.colab import drive
drive.mount('https://drive.google.com/file/d/1KxwFsL6IF7OD_XN28kjxl0-amnELIhZ8/view?usp=sharing')
#get the maximum temparature 
df['Temperature'].max()
#to know which day it rains
df['EST'][df['Events'] == 'Rain']
#3. average wind speed
df['WindSpeedMPH'].mean()

# Installation


