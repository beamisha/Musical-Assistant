import sys
import json

# Get the first command-line argument
command = sys.argv[1]

# Load the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

with open('running.json', 'r') as file:
    running = json.load(file)

index = running["index"]

print('here1')
print(command)

if command=='n':
    print('here2')
    displaying = data[index]["displaying"]
    split_txt = "("+data[index]["current_section"]+")"
    splitted_string = displaying.split(split_txt, 1)
    data[index]["displaying"] = splitted_string[-1]

# Save the updated JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

