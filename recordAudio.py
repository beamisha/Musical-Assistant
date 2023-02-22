import sys
import subprocess
import time
import signal

# Get the first command-line argument
song = sys.argv[1]
duration = sys.argv[2]

output_file = song+".m4a"

command = ["ffmpeg", "-f", "avfoundation", "-i", ":0", output_file]
process = subprocess.Popen(command)

# wait for the specified duration
time.sleep(int(duration))

# stop recording
process.send_signal(signal.SIGINT)
