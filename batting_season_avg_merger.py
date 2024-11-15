# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 02:01:21 2024

@author: skrut
"""
import csv

name_id_map = {}
with open('2023allplayers.csv', 'r') as name_file:  
    name_reader = csv.DictReader(name_file)
    for row in name_reader:
        # Create full name and map it to the player ID
        name_id_map[row['id']] = f"{row['first']} {row['last']}"
        
# Initialize dictionaries for aggregated statistics
season_avg_data = {}

# Process input file to calculate season averages
with open('2023_merged_batting_data.csv', 'r') as stat_file:
    stat_reader = csv.DictReader(stat_file)
    header = stat_reader.fieldnames + ['season_batting_avg']

    # Step 1: Accumulate stats for each player
    for row in stat_reader:
        name = row['id']
        bats = int(row['b_ab'])
        hits = int(row['b_h'])

        if name in season_avg_data:
            season_avg_data[name]['total_at_bats'] += bats
            season_avg_data[name]['total_hits'] += hits
        else:
            season_avg_data[name] = {'total_at_bats': bats, 'total_hits': hits}

# Step 2: Write updated rows with season averages
updated_rows = []
with open('2023_merged_batting_data.csv', 'r') as stat_file:
    stat_reader = csv.DictReader(stat_file)
    for row in stat_reader:
        name = row['id']
        total_bats = season_avg_data[name]['total_at_bats']
        total_hits = season_avg_data[name]['total_hits']

        # Calculate batting average and handle division by zero
        batting_average = total_hits / total_bats
        

        # Add season average to the row
        row['season_batting_avg'] = f"{batting_average:.3f}"
        

        updated_rows.append(row)


# Step 3: Write to a new CSV file
with open('2023_complete_batting_data.csv', 'w', newline='') as updated_file:
    writer = csv.DictWriter(updated_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(updated_rows)

