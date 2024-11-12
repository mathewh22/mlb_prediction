# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:22:46 2024

@author: skrut
"""

import pandas as pd

# Load your CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Specify the columns you want to keep
columns_to_keep = ['column1', 'column2', 'column3']  # Replace with your column names

# Create a new DataFrame with only the selected columns
df_filtered = df[columns_to_keep]

# Optionally, save the filtered DataFrame to a new CSV
df_filtered.to_csv('filtered_file.csv', index=False)

# Print the filtered DataFrame to verify
print(df_filtered)
