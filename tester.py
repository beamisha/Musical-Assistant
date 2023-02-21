import json

with open('sections.json', 'r') as file:
    sectionNames = json.load(file)

keys = ["i", "v", "c", "b", "o"]

lyricsTest = "[[v]] I | I (4 bars) Hey Jude, don’t be afraid, you were made to go out and get her (v) I | I (4 bars) Hey Jude, don’t be afraid, you were made to go out and get her (v) [[v]]"

def countSections(structure, sectionType):
    count = 0
    for section in structure:
        if section == sectionType:
            count += 1
    return count

print(lyricsTest)
numSections = {}
for key in keys:
    numSections[key] = countSections(["v", "v"], key)
    print(key)
    print(numSections[key])
    for i in range(0,numSections[key]):
        lyricsTest = lyricsTest.replace("[["+key+"]]", sectionNames[key]+" "+str(i+1)+"/"+str(numSections[key]), 1)

print(lyricsTest)