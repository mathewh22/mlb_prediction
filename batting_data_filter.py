# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:22:46 2024

@author: skrut
"""

import pandas as pd

# Load your CSV file into a DataFrame
df = pd.read_csv('2023batting.csv')

# Specify the columns you want to keep
columns_to_keep = ['gid', 'id', 'team', 'b_pa', 'b_ab', 'b_h', 'b_d', 'b_t', 'b_hr', 'b_rbi', 'b_w', 'b_k', 'date', 'wl']  # Replace with your column names

# Create a new DataFrame with only the selected columns
df_filtered = df[columns_to_keep]

# Optionally, save the filtered DataFrame to a new CSV
df_filtered.to_csv('2023_filtered_batting_data.csv', index=False)

# Print the filtered DataFrame to verify
#print(df_filtered)
