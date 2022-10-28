message = 'My name is AL SWEIGART and I am 4,000 years old.'
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

result = []
for word in message.split():

    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    # If the first charcter of the word is not a letter, then leave the word as it is
    if not word[0].isalpha():
        word = word

    # If the last character of the word is not a letter, then place it at the end of the word
    elif not word[-1].isalpha():
        punc = word[-1]
        word = word[:-1]
        if word[0].lower() in VOWELS:
            word += 'yay'
        else:
            letter = word[0]
            word = word[1:] + letter + 'ay'
        word = word + punc
    
    elif word[0].lower() in VOWELS:
        word += 'yay'
    else:
        letter = word[0]
        word = word[1:] + letter + 'ay'

    if wasUpper:
        word = word.upper()
    
    if wasTitle:
        word = word.title()

    result.append(word)

print(' '.join(result))

