import pyinputplus as pyip
import re

f = open('9-MadLibInputFile.txt', 'r')
o = open('9-MadLibOutputFile.txt', 'w')

words = f.read()
regex = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)')
matches = regex.findall(words)

for match in matches:
    word = pyip.inputStr(f'Enter a(n) {match.lower()}:')
    words = words.replace(match, word, 1)

o.write(words)
print(words)
f.close()
o.close()

