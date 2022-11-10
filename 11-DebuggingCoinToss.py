import random, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)

def checkGuessInput():
    guess = ''

    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    if guess == 'heads':
        guess = 1
    elif guess == 'tails':
        guess = 0

    return guess

myGuess = checkGuessInput()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('toss is: ' + str(toss))

logging.debug('My 1st guess is: ' + str(myGuess))

if toss == myGuess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    myGuess = checkGuessInput()

    logging.debug('my 2nd guess is: ' + str(myGuess))

    if toss == myGuess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')