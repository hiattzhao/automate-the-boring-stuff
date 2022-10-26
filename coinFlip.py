import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    values = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            values.append("H")
        else:
            values.append("T")

    #print(values)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for index in range(100):
        if (values[index: index+6] == ['H', 'H', 'H', 'H', 'H', 'H']):
            numberOfStreaks += 1
        elif (values[index: index+6] == ['T', 'T', 'T', 'T', 'T', 'T']):
            numberOfStreaks += 1
#print("Chance of streak: %s%%" % (numberOfStreaks / 1))
print("Chance of streak: " + str(numberOfStreaks /10000) + "%")
