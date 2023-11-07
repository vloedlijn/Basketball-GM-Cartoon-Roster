import json
import os
import subprocess
from cairosvg import svg2png
from datetime import datetime

def convert_json_to_svg_to_png(player_id):
    # Path to player's folder and files
    player_folder = f'players/{player_id}'
    json_path = f'{player_folder}/{player_id}.json'
    png_path = f'{player_folder}/{player_id}.png'
    
    # Read the JSON data
    with open(json_path, 'r') as file:
        player_data = json.load(file)
    
    # Convert the JSON to an SVG string using the Node.js script
    result = subprocess.run(['node', 'src/runBuildSVGString.js'], input=json.dumps(player_data), text=True, capture_output=True)
    svg_string = result.stdout
    
    # Convert the SVG string to a PNG file using cairosvg or any other library
    if len(svg_string) > 0:
        svg2png(bytestring=svg_string, write_to=png_path)
    else:
        print(f'No SVG string for {player_id}')

def update_player_images():
    # Get all player folders in the 'players' directory
    for player_id in os.listdir('players'):
        player_folder = os.path.join('players', player_id)
        
        # Check if folder is a directory
        if os.path.isdir(player_folder):
            json_path = os.path.join(player_folder, f'{player_id}.json')
            png_path = os.path.join(player_folder, f'{player_id}.png')

            # Check existence and modification time
            json_exists = os.path.isfile(json_path)
            png_exists = os.path.isfile(png_path)
            
            if json_exists and (not png_exists or os.path.getmtime(png_path) < os.path.getmtime(json_path)):
                print(f"Updating image for {player_id}")
                convert_json_to_svg_to_png(player_id)
            elif not json_exists:
                print(f"JSON file for {player_id} does not exist.")
            else:
                print(f"PNG for {player_id} is up to date.")

# Call the function to update player images
update_player_images()
