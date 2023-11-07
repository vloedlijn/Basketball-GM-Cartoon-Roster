import json
import os

# Define the path to the source JSON file and the target directory
source_file = "PlayerFaceBySRID-22-23CartoonRosterPostDraft.json"
target_dir = "players"

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)

# Read the source JSON file
with open(source_file, 'r') as file:
    players_data = json.load(file)

# Loop through the players_data dictionary
for player_id, player_info in players_data.items():
    # Create a directory for each player_id within the 'players' directory
    player_dir = os.path.join(target_dir, player_id)
    os.makedirs(player_dir, exist_ok=True)
    
    # Define the path for the player's individual JSON file
    player_file_path = os.path.join(player_dir, f"{player_id}.json")
    
    # Write the player_info to the player's JSON file
    with open(player_file_path, 'w') as player_file:
        json.dump(player_info, player_file, indent=4)

print("JSON files for all players have been created successfully.")
