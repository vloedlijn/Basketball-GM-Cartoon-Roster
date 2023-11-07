import json
import requests

# Load the CombinedPlayerFaces.json file
with open('CombinedPlayerFaces.json', 'r') as file:
    combined_player_faces = json.load(file)

# Download the roster file
roster_url = ""
roster_response = requests.get(roster_url)

# Make sure the request was successful
if roster_response.status_code == 200:
    # Parse the downloaded file as JSON
    roster_data = roster_response.json()

    # Get the srID values from the "players" list in the roster data
    roster_srIDs = {player['srID'] for player in roster_data['players'] if 'srID' in player}

    print('roster_srIDs', roster_srIDs, roster_data)

    # Find any srIDs that are not in the CombinedPlayerFaces.json keys
    missing_srIDs = roster_srIDs - set(combined_player_faces.keys())

    # Write the missing srIDs to a JSON file
    with open('missingPlayerSRIDs.json', 'w') as outfile:
        json.dump(list(missing_srIDs), outfile, indent=4)

    # Print the result
    if missing_srIDs:
        print("Missing srIDs written to missingPlayerSRIDs.json")
    else:
        print("No missing srIDs found. All players are present in CombinedPlayerFaces.json.")
else:
    print("Failed to download the file. HTTP Status Code:", roster_response.status_code)
