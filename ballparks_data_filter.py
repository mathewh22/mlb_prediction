# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:22:46 2024

@author: skrut
"""

import pandas as pd

# load csv file
df = pd.read_csv('ballparks.csv')

# keep wanted data columns
columns_to_keep = ['team_name', 'ballpark', 'left_field', 'center_field', 'right_field', 'min_wall_height', 'max_wall_height']  

# new data frame
df_filtered = df[columns_to_keep]

# save new csv file
df_filtered.to_csv('2023_filtered_ballpark_data.csv', index=False)

