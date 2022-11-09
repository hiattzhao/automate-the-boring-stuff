import os
from pathlib import Path

currentDirectory = Path.cwd()
size = 400000
for folders, subfolders, filenames in os.walk(currentDirectory):
    for filename in filenames:
        if os.path.getsize(os.path.join(folders, filename)) > size:
            print (filename + ' in ' + folders + ' is greater than ' + str(size))

print('Done!')