# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:22:46 2024

@author: skrut
"""

import pandas as pd

# load csv file
df = pd.read_csv('2023batting.csv')

# keep wanted data columns
columns_to_keep = ['gid', 'id', 'team', 'b_pa', 'b_ab', 'b_h', 'b_d', 'b_t', 'b_hr', 'b_rbi', 'b_w', 'b_k', 'date', 'wl']  # Replace with your column names

# new data frame
df_filtered = df[columns_to_keep]

# save new csv file
df_filtered.to_csv('2023_filtered_batting_data.csv', index=False)

