# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:22:46 2024

@author: skrut
"""

import pandas as pd

# load csv file
df = pd.read_csv('2023pitching.csv')

# keep wanted data columns
columns_to_keep = ['gid', 'id', 'team', 'p_seq', 'p_h', 'p_r', 'p_er', 'p_w', 'p_hbp', 'p_wp', 'date', 'wl']  

# new data frame
df_filtered = df[columns_to_keep]

# save filtered csv file
df_filtered.to_csv('2023_filtered_pitching_data.csv', index=False)

