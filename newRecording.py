import sys
import json
import subprocess
import signal
import time

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
    start = sequence[0][1]
    stop = sequence[-1][1]

    print("Start:",start)
    print("Stop:",stop)

    process1 = subprocess.Popen(["SwitchAudioSource", "-s", "BlackHole 2ch"])

    process2 = subprocess.Popen(["SwitchAudioSource", "-t", "input", "-s" "BlackHole 2ch"])

    # Start subprocess 1
    process3 = subprocess.Popen(['python', 'midiPlayer.py', song])

    # wait for the specified duration
    time.sleep(start/1000)

    duration = int((stop/1000)-(start/1000))
    # Start subprocess 2
    process4 = subprocess.Popen(['python', 'recordAudio.py', song, str(duration)])

    # wait for the specified duration
    time.sleep(duration+1)

    process1.send_signal(signal.SIGINT)

    process2.send_signal(signal.SIGINT)

    process3.send_signal(signal.SIGINT)

    process4.send_signal(signal.SIGINT)