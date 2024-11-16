# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:36:19 2024

@author: skrut
"""

import csv 
from datetime import datetime

name_id_map = {}
with open('2023allplayers.csv', 'r') as name_file:  
    name_reader = csv.DictReader(name_file)
    for row in name_reader:
        # Create full name and map it to the player ID
        name_id_map[row['id']] = f"{row['first']} {row['last']}"

# Step 2: Read the baseball data file and replace IDs with full names
updated_rows = []
with open('2023_complete_pitching_data.csv', 'r') as data_file: 
    data_reader = csv.reader(data_file)
    header = next(data_reader)  
    updated_rows.append(header)

    for row in data_reader:
        
        date_str = row[11]
        date_format = datetime.strptime(date_str, '%Y%m%d').strftime('%m/%d/%Y')
        row[11] = date_format
        
        player_id = row[1]  #'id' is in the second column
        if player_id in name_id_map:
            row[1] = name_id_map[player_id]  # Replace ID with full name
        updated_rows.append(row)

# Step 3: Write the updated data to a new CSV file
with open('2023_full_pitching_stats_cleaned.csv', 'w', newline='') as updated_file:
    writer = csv.writer(updated_file)
    writer.writerows(updated_rows)