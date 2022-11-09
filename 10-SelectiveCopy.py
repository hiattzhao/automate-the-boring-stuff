import shutil, os
from pathlib import Path

# Search for all files with a certain file extension in a folder
currentDirectory = Path.cwd()

for folderName, subfolders, filenames in os.walk(currentDirectory):
    for filename in filenames:
        if filename.endswith('pdf'):
            shutil.copy(currentDirectory / filename, currentDirectory / '10-BackupFolder')

print('Done copying')

