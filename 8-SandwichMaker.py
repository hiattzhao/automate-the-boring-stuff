import pyinputplus as pyip

price = 1.00

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], 'bread type:\n', numbered = True)

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], 'protein type:\n', numbered = True)
if protein == 'chicken' or 'turkey' or 'ham':
    price += 2
elif protein == 'tofu':
    price += 1.50

cheese = pyip.inputYesNo('want cheese?\n')
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], 'cheese type:\n', numbered = True)
    price += 1
else:
    cheeseType = 'no cheese'
stuff = pyip.inputYesNo('want mayo, mustard, lettuce, or tomato?\n')
if stuff == 'yes':
    price += 2
    everything = 'with everything'
else:
    everything = 'without mayo, mustard, lettuce, or tomato'
amount = pyip.inputInt('how many sandwiches?\n', min = 1)
if amount > 1:
    price *= amount

print(f'You have ordered {amount} sandwich(es) with {bread}, {protein}, {cheeseType}, {everything}. The price is ${price: .2f}')