import re

def regexStrip(text, character = ''):
    if character == '': 
        regexText = re.compile(r'\s')
        print(regexText.sub('',text))
    else:
        regexText = re.compile(r'[%s]' %character)
        print(regexText.sub('', text))


regexStrip(' test ')
regexStrip('test', 't')
regexStrip('test', 'z')