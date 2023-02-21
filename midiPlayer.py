import time
import json
import sys
import subprocess

# Get the first command-line argument
song = sys.argv[1]

with open('midiData/notes.json', 'r') as file:
    notes = json.load(file)

with open('midiData/metaNotes.json', 'r') as file:
    metaNotes = json.load(file)

index = 10000
for i in range(0,len(metaNotes)) :
    if metaNotes[i] == song:
        index = i

if index == 10000:
    print("Song not found")
else:
    sequence = notes[index]
    sequenceLength = len(sequence)
    print(sequenceLength)
    # Get the current time
    start_time = time.time() * 1000
    count = 0
    while True:
        note = sequence[count][0][1]
        noteTime = sequence[count][1]
        # Get the current time
        current_time = time.time() * 1000
        elapsed = current_time - start_time
        # Check if the time interval has elapsed
        
        if (int(elapsed) == noteTime):
            print("Elapsed: "+str(elapsed))
            print("noteTime: "+str(noteTime))
            # Perform the desired action
            if note == 24:
                subprocess.Popen(["python", "notePlayer.py", "one"])      
            if note == 26:
                subprocess.Popen(["python", "notePlayer.py", "two"])
            if note == 28:
                subprocess.Popen(["python", "notePlayer.py", "three"])
            if note == 29:
                subprocess.Popen(["python", "notePlayer.py", "four"])
            if note == 31:
                subprocess.Popen(["python", "notePlayer.py", "five"])
            if note == 33:
                subprocess.Popen(["python", "notePlayer.py", "six"])
            if note == 35:
                subprocess.Popen(["python", "notePlayer.py", "seven"])
            if note == 36:
                subprocess.Popen(["python", "notePlayer.py", "eight"])
            print(str(note)+" played at "+str(elapsed) + "ms")
            if count == (sequenceLength-1) :
                print("here")
                break
            count+=1