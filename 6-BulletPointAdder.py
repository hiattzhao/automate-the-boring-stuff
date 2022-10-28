#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

"""
Run in Terminal:
1. cd /Users/hiattzhao/Documents/automate-the-boring-stuff
2. source venv/bin/activate
3. Copy the following:
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
4. python3 6-BulletPointAdder.py
5. Paste to a text editor. Should see the bulleted list:
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
"""

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)