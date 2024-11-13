# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:22:46 2024

@author: skrut
"""

import pandas as pd

# Load your CSV file into a DataFrame
df = pd.read_csv('2023pitching.csv')

# Specify the columns you want to keep
columns_to_keep = ['gid', 'id', 'team', 'p_seq', 'p_h', 'p_r', 'p_er', 'p_w', 'p_hbp', 'p_wp', 'date', 'wl']  # Replace with your column names

# Create a new DataFrame with only the selected columns
df_filtered = df[columns_to_keep]

# Optionally, save the filtered DataFrame to a new CSV
df_filtered.to_csv('2023_filtered_pitching_data.csv', index=False)

# Print the filtered DataFrame to verify
#print(df_filtered)
