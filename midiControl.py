import pygame.midi
import subprocess

import simpleaudio as sa

# Load audio file
wave_obj = sa.WaveObject.from_wave_file('audio/9_theo_5.wav')

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

bpm = 30
millis = int(60000 / bpm)
nextTime = millis
# Start an infinite loop to receive MIDI messages
while True:
    if midi_in.poll():
        # Receive a list of MIDI events (timestamp, status, data1, data2)
        midi_events = midi_in.read(10)
        
        # Print the MIDI events to the console
        for midi_event in midi_events:
            if (nextTime < midi_event[1]) :
                play_obj = wave_obj.play()
                play_obj.wait_done()
                nextTime += millis
            if midi_event[0][0] == 147 :
                # Run the script with command-line arguments
                subprocess.run(['python', 'execute.py', 'n'])
                print("running!")
                break
            print(midi_event)


# Close the MIDI input device and quit pygame.midi
midi_in.close()
pygame.midi.quit()