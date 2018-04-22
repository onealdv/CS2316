import pandas as pd
import numpy as np

#required: south-atlantic-water-temps.csv file
water_temps = pd.read_csv("south-atlantic-water-temps.csv",index_col = 0)

#adds 'avg' column to dataframe
water_temps['avg'] = water_temps.apply(np.mean,axis = 1)

#Gives coldest temperature in Jan
coldest_jan_temp = water_temps['JAN'].min()

#Gives warmest temperature in Nov
warmest_nov = water_temps['NOV'][water_temps['NOV'] == water_temps['NOV'].max()]
