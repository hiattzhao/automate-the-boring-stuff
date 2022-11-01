import re

def testPassword(password):
    passwordRegex = re.compile(r'[a-zA-Z|\d]{8,}')
    mo = passwordRegex.search(password)
    try:
        if mo.group():
            print('You have a strong password')
    except AttributeError:
        print('You have a weak password')

testPassword('testpw')
testPassword('Testpw')
testPassword('1TESTPWRT')
testPassword('TESTPW123')
testPassword('Testpw123')
testPassword('TESTPW123!@#')
testPassword('Tb1@Tb1@')
testPassword('TestPW123')
testPassword('!@345ssfe@#23T4')
testPassword('')