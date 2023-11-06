import json

input_file_name = '22-23CartoonRosterPostDraft.json'
# Open the input file and load its contents
with open(input_file_name, 'r') as f:
    fj = json.load(f)

# Create a dictionary of players with their 'srID' as keys if 'face' and 'srID' are present
player_json = {p['srID']: p['face'] for p in fj['players'] if 'face' in p and 'srID' in p}
for srID in player_json:
    p = player_json[srID]
    del p['teamColors']

# Create a list of players without a 'face' entry
no_face = [{"pid": p.get('pid'), 'srID': p.get('srID')} for p in fj['players'] if 'face' not in p]

# Use a with-statement to open the file for writing, this ensures the file is properly closed after the block's execution
with open(f'PlayerFaceBySRID-{input_file_name}', 'w') as fo:
    json.dump(player_json, fo, indent=1)

with open(f'faces_to_add/PlayerFaceBySRID-{input_file_name}', 'w') as fo:
    json.dump(no_face, fo, indent=1)

# Optionally, uncomment these lines if you wish to print out the contents to the console
# print(json.dumps(player_json, indent=2))
# print(json.dumps(no_face, indent=2))
