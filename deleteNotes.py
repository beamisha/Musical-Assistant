import json
import sys

# Get the first command-line argument
song = sys.argv[1]

with open('midiData/notes.json', 'r') as file:
    notes = json.load(file)

with open('midiData/metaNotes.json', 'r') as file:
    metaNotes = json.load(file)

count = 0
for str in metaNotes:
    if str == song:
        notes.pop(count)
        metaNotes.pop(count)
    count += 1

with open('midiData/notes.json', 'w') as file:
    json.dump(notes, file, indent=2)

with open('midiData/metaNotes.json', 'w') as file:
    json.dump(metaNotes, file, indent=2)