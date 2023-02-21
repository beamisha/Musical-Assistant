import sys
import subprocess
import time
import signal

# Get the first command-line argument
song = sys.argv[1]

process1 = subprocess.Popen(["SwitchAudioSource", "-s", "BlackHole 2ch"])

process2 = subprocess.Popen(["SwitchAudioSource", "-t", "input", "-s" "BlackHole 2ch"])

# Start subprocess 1
process3 = subprocess.Popen(['python', 'midiPlayer.py', song])

# Start subprocess 2
process4 = subprocess.Popen(['python', 'recordAudio.py', song])

duration = 11

# wait for the specified duration
time.sleep(duration)

process1.send_signal(signal.SIGINT)

process2.send_signal(signal.SIGINT)

process3.send_signal(signal.SIGINT)

process4.send_signal(signal.SIGINT)