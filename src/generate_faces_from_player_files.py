import json
import os

print("Current Working Directory:", os.getcwd())
# Define the path to the target JSON file and the source directory
target_file = "CombinedPlayerFaces.json"
source_dir = "players"

# Prepare a dictionary to hold all player data
all_players_data = {}

# Iterate over each directory in the source directory
for player_id in os.listdir(source_dir):
    player_dir = os.path.join(source_dir, player_id)
    # Check if it's actually a directory
    if os.path.isdir(player_dir):
        # Construct the file path assuming the file is named as per the folder
        player_file_path = os.path.join(player_dir, f"{player_id}.json")
        # Check if the JSON file exists
        if os.path.isfile(player_file_path):
            # Open the player's JSON file and load the data
            with open(player_file_path, 'r') as player_file:
                try:
                    player_data = json.load(player_file)
                    # Add the player's data to the all_players_data dictionary
                    all_players_data[player_id] = player_data
                except json.JSONDecodeError as e:
                    print(f"Error reading {player_file_path}: {e}")

sorted_all_players_data = {player_id: all_players_data[player_id] for player_id in sorted(all_players_data)}

# Write the combined data to the target JSON file
with open(target_file, 'w') as file:
    json.dump(sorted_all_players_data, file, indent=4)

print("All player data has been combined into one JSON file successfully.")
