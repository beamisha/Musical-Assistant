import json

with open('data.json', 'r') as file:
    data = json.load(file)

with open('sections.json', 'r') as file:
    sectionNames = json.load(file)

keys = ["i", "v", "c", "b", "o"]

title = input("Enter the name of the song")
time = input("Enter the time signature (e.g. '4/4')")
structure = []
lnLengths = []
lyrics = ""
while True:
    print("This song currently has the following structure:")
    print(structure)
    decision1 = input("Would you like to add a section to this song? (y/n)")
    
    if decision1 == "n":
        break
    elif decision1 == "y":
        sectionType = input("Enter the type of the first section (i, v, c, b, o)")
        lnLength = input("Enter the number of bars in a line of this section")
        chords = input("Enter the chords for a line in this section as roman numerals separated by '|' (e.g. 'I | I | ii V |)")
        section = "[["+sectionType+"]]\n\n"
        while True:
            decision2 = input("Would you like to add a line to this section? (y/n)")
            if decision2 == "n":
                break
            elif decision2 == "y":
                line = input("Enter the line")
                section += chords+" ("+lnLength+" bars)"+"\n"+line+" ("+sectionType+")"+"\n\n"
        structure.append(sectionType)
        lnLengths.append(lnLength)
        lyrics += section

def countSections(structure, sectionType):
    count = 0
    for section in structure:
        if section == sectionType:
            count += 1
    return count

lyricsTest = "[[v]] I | I (4 bars) Hey Jude, don’t be afraid, you were made to go out and get her (v) I | I (4 bars) Hey Jude, don’t be afraid, you were made to go out and get her (v) [[v]]"

numSections = {}
for key in keys:
    numSections[key] = countSections(structure, key)
    print(key)
    print(numSections[key])
    for i in range(0,numSections[key]):
        lyrics = lyrics.replace("[["+key+"]]", sectionNames[key]+" "+str(i+1)+"/"+str(numSections[key]), 1)

modifiedTitle = (title.replace(" ", "_")).lower()
filePath = "lyrics/"+modifiedTitle+".txt"

tempo = input("What is the tempo?")
newSong = {
    "lnLengths": lnLengths,
    "current_section": structure[0], 
    "lyrics": filePath, 
    "tempo" : tempo,
    "title": title, 
    "displaying": "",
    "sections": structure,
}

data.append(newSong)

# Open the file for writing
with open(filePath, "w") as file:
    # Write to the file
    file.write(lyrics)

with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

print(lyrics)