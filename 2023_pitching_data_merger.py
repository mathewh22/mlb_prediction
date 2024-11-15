# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:59:42 2024

@author: skrut
"""

import csv

# load ball park data into a dictionary
stadium_data = {}
with open('2023_filtered_ballpark_data.csv', 'r') as stadium_file:  
    stadium_reader = csv.DictReader(stadium_file)
    for row in stadium_reader:
        team_name = row['team_name']  
        stadium_data[team_name] = row  
        
gameinfo_data = {}
with open('2023_filtered_gameinfo_data.csv', 'r') as gameinfo_file:  
    gameinfo_reader = csv.DictReader(gameinfo_file)
    for row in gameinfo_reader:
        gid = row['gid']  
        gameinfo_data[gid] = row  
        

# read batting data, merge with ball park data, store updated rows
updated_rows = []
with open('2023_filtered_pitching_data.csv', 'r') as game_log_file: 
    batting_log = csv.reader(game_log_file)
    header = next(batting_log)  # Capture the header row
    # add new ball park data columns to the header row
    stadium_columns = list(stadium_data.values())[0].keys()  
    gameinfo_columns = list(gameinfo_data.values())[0].keys()
    new_gameinfo_columns = []
    
    for col in gameinfo_columns:
        if col != 'gid':
            new_gameinfo_columns.append(col)
                
    updated_rows.append(header + list(stadium_columns) + new_gameinfo_columns)

    for row in batting_log:
        gid = row[0]  
        team_id = gid[:3]  # Extract the first three characters as team_id

        if team_id in stadium_data:
            
            stadium_info = stadium_data[team_id]
            row.extend(stadium_info.values())
        
        if gid in gameinfo_data:
            
            gameinfo = gameinfo_data[gid]
            updated_gameinfo = []
            for key, value in gameinfo.items():
                if key != 'gid':
                    updated_gameinfo.append(value)
            row.extend(updated_gameinfo)
            
        updated_rows.append(row)


# new csv file output
with open('2023_merged_pitching_data.csv', 'w', newline='') as updated_file:
    writer = csv.writer(updated_file)
    writer.writerows(updated_rows)