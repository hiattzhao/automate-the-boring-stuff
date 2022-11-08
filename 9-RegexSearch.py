from pathlib import Path
import re

currentDirectory = Path.cwd()
txtFiles = list(currentDirectory.glob('*File.txt'))

print(f'Your current directory is: {currentDirectory}')

userInput = input('What is the regex to search?\n')
regex = re.compile(userInput)
foundMatches = []

for txtFile in txtFiles:
    f = open(txtFile, 'r')
    matches = regex.findall(f.read())

    if matches:
        foundMatches.append(matches)

    f.close()

print(foundMatches)