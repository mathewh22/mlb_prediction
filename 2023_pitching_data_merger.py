# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:59:42 2024

@author: skrut
"""

import csv

# load ball park data into a dictionary
stadium_data = {}
with open('ballparks.csv', 'r') as stadium_file:  
    stadium_reader = csv.DictReader(stadium_file)
    for row in stadium_reader:
        team_name = row['team_name']  
        stadium_data[team_name] = row  

# read batting data, merge with ball park data, store updated rows
updated_rows = []
with open('2023_pitching_data_cleaned.csv', 'r') as game_log_file: 
    batting_log = csv.reader(game_log_file)
    header = next(batting_log)  # Capture the header row
    # add new ball park data columns to the header row
    stadium_columns = list(stadium_data.values())[0].keys()  
    updated_rows.append(header + list(stadium_columns))

    for row in batting_log:
        gid = row[0]  # Assuming game_id is in the first column
        team_id = gid[:3]  # Extract the first three characters as team_id

        if team_id in stadium_data:
            
            stadium_info = stadium_data[team_id]
            row.extend(stadium_info.values())
    
        updated_rows.append(row)

# new csv file output
with open('2023_merged_pitching_data.csv', 'w', newline='') as updated_file:
    writer = csv.writer(updated_file)
    writer.writerows(updated_rows)