# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:38:09 2024

@author: skrut
"""

import csv
from datetime import datetime

# Step 1: Load the player names into a dictionary
name_id_map = {}
with open('2023allplayers.csv', 'r') as name_file:  
    name_reader = csv.DictReader(name_file)
    for row in name_reader:
        # Create full name and map it to the player ID
        name_id_map[row['id']] = f"{row['first']} {row['last']}"

# Step 2: Read the baseball data file and replace IDs with full names
updated_rows = []
with open('2023_filtered_batting_data.csv', 'r') as data_file:  
    data_reader = csv.reader(data_file)
    header = next(data_reader)  
    updated_rows.append(header)

    for row in data_reader:
        
        if int(row[3]) == 0:  # Adjust index if necessary
            continue  # Skip rows with zero plate appearances
            
        date_str = row[12]
        date_format = datetime.strptime(date_str, '%Y%m%d').strftime('%m/%d/%Y')
        row[12] = date_format
        
        player_id = row[1]  # 'id' is in the second column
        if player_id in name_id_map:
            row[1] = name_id_map[player_id]  # Replace ID with full name
        
        updated_rows.append(row)


# Step 3: Write the updated data to a new CSV file
with open('2023_batting_data_cleaned.csv', 'w', newline='') as updated_file:
    writer = csv.writer(updated_file)
    writer.writerows(updated_rows)


