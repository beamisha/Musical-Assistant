import sys
import json
import re

# Get the first command-line argument
song = sys.argv[1]

with open('data.json', 'r') as file:
    data = json.load(file)

with open('running.json', 'r') as file:
    running = json.load(file)

songTitle = song.replace("_", " ")
index = 0
for i in range(0,len(data)) :
    if (data[i]["title"].lower() == songTitle) :
        index = i

lyricsFile = data[index]["lyrics"]

with open(lyricsFile, "r") as file:
    lyrics = file.read()

lyrics = re.sub(' +', ' ', lyrics)

lnLengths = data[index]["lnLengths"]
for i in range(0,len(lnLengths)) :
    lyrics = lyrics.replace("length"+str(i), str(lnLengths[i])+" bars")
    
data[index]["displaying"] = lyrics
running["index"] = index

# Save the updated JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)
