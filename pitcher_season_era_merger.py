# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:45:10 2024

@author: skrut
"""

import csv

# Initialize dictionaries for aggregated statistics
season_avg_data = {}

# Process input file to calculate season averages
with open('2023_merged_pitching_data.csv', 'r') as stat_file:
    stat_reader = csv.DictReader(stat_file)
    header = stat_reader.fieldnames + ['season_era']

    # Step 1: Accumulate stats for each player
    for row in stat_reader:
        name = row['id']
        outs = int(row['p_ipouts'])
        era = int(row['p_er'])

        if name in season_avg_data:
            season_avg_data[name]['total_innings'] += (outs / 3)
            season_avg_data[name]['total_earned_runs'] += era
        else:
            season_avg_data[name] = {'total_innings': (outs / 3), 'total_earned_runs': era}

# Step 2: Write updated rows with season averages
updated_rows = []
with open('2023_merged_pitching_data.csv', 'r') as stat_file:
    stat_reader = csv.DictReader(stat_file)
    for row in stat_reader:
        name = row['id']
        innings = season_avg_data[name]['total_innings']
        earned_runs = season_avg_data[name]['total_earned_runs']

        # Calculate season era
        season_era =  9 * (earned_runs / innings)
        

        # Add season average to the row
        row['season_era'] = f"{season_era:.3f}"
        updated_rows.append(row)

# Step 3: Write to a new CSV file
with open('2023_complete_pitching_data.csv', 'w', newline='') as updated_file:
    writer = csv.DictWriter(updated_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(updated_rows)
