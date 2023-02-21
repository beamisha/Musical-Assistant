import sys
import json

# Get the first command-line argument
song = sys.argv[1]

# Load the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

songTitle = song.replace("_", " ")
index = 0
for i in range(0,len(data)) :
    if (data[i]["title"].lower() == songTitle) :
        index = i

data[index]["displaying"] = ""
data[index]["running"] = "false"

# Save the updated JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)