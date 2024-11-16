# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:38:09 2024

@author: skrut
"""

import csv

updated_rows = []
with open('2023_filtered_batting_data.csv', 'r') as data_file:  
    data_reader = csv.reader(data_file)
    header = next(data_reader)  
    updated_rows.append(header)

    for row in data_reader:
        
        if int(row[3]) == 0:  # Adjust index if necessary
            continue  # Skip rows with zero plate appearances
            
        updated_rows.append(row)


# Step 3: Write the updated data to a new CSV file
with open('2023_batting_data_cleaned.csv', 'w', newline='') as updated_file:
    writer = csv.writer(updated_file)
    writer.writerows(updated_rows)



