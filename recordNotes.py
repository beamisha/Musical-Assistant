import pygame.midi
import subprocess
import simpleaudio as sa
import json
import sys
import time

# Get the first command-line argument
song = sys.argv[1]

with open('midiData/notes.json', 'r') as file:
    notes = json.load(file)

with open('midiData/metaNotes.json', 'r') as file:
    metaNotes = json.load(file)

index = len(notes)
metaNotes.append(song)

# Initialize the pygame.midi module
pygame.midi.init()

# Print the number of available input devices
num_devices = pygame.midi.get_count()
print("Number of available input devices:", num_devices)

# Open the first available input device
device_id = 0
midi_in = pygame.midi.Input(device_id)

# Print the name of the input device
device_info = pygame.midi.get_device_info(device_id)
device_name = device_info[1].decode("utf-8")
print("Using MIDI input device:", device_name)

process1 = subprocess.Popen(["SwitchAudioSource", "-s", "BlackHole 2ch"])

sequence = []
stopped = False
oldTime = 0
threshold = 400
bpm = 120
millisPerBeat = int(60000/bpm)
print("BPM:",bpm)
print("Milliseconds per beat:",millisPerBeat)

start_time = time.time()
# Start an infinite loop to receive MIDI messages
while True:
    if midi_in.poll():
        # Receive a list of MIDI events (timestamp, status, data1, data2)
        midi_events = midi_in.read(10)
        # Print the MIDI events to the console
        for midi_event in midi_events:
            
            if midi_event[0][0] in [147] :
                newTime = midi_event[1]
                if (newTime - oldTime) > threshold :
                    if midi_event[0][1] == 52 :
                        print(midi_event)
                        print("Starting!")
                    sequence.append(midi_event)
                    # Run the script with command-line arguments
                    print("Recorded event!")
                    print(midi_event)
                if midi_event[0][1] == 60 :
                    print(midi_event)
                    print("Stopping!")
                    stopped = True
                    break
                oldTime = newTime
            print(midi_event)
        if stopped:
            break

notes.append(sequence)

# Close the MIDI input device and quit pygame.midi
midi_in.close()
pygame.midi.quit()

with open('midiData/notes.json', 'w') as file:
    json.dump(notes, file, indent=2)

with open('midiData/metaNotes.json', 'w') as file:
    json.dump(metaNotes, file, indent=2)
