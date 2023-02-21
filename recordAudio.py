import sys
import subprocess
import time
import signal

# Get the first command-line argument
song = sys.argv[1]

output_file = song+".m4a"
duration = 10 # duration of recording in seconds

command = ["ffmpeg", "-f", "avfoundation", "-i", ":0", output_file]
process = subprocess.Popen(command)

# wait for the specified duration
time.sleep(duration)

# stop recording
process.send_signal(signal.SIGINT)
