# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:22:46 2024

@author: skrut
"""

import pandas as pd

# load csv file
df = pd.read_csv('2023gameinfo.csv')

# keep wanted data columns
columns_to_keep = ['gid', 'daynight', 'attendance', 'precip', 'sky', 'temp', 'winddir', 'windspeed']  

# new data frame
df_filtered = df[columns_to_keep]

# save new csv file
df_filtered.to_csv('2023_filtered_gameinfo_data.csv', index=False)

