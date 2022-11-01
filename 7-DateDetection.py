import re

dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
mo = dateRegex.search('11/31/2002')
month = mo.group(1)
day = mo.group(2)
year = mo.group(3)
print(mo.group())
print('month: ' + month)
print('day: ' + day)
print('year: ' + year)

isValidDate = True
if int(month) not in range(1,12):
    print('Month is out of range')
    isValidDate = False
# For month in April, June..., Day can not be longer than 30
elif int(month) in [4, 6, 9, 11]:
    if int(day) > 30:
        print('Day is out of range for month with 30 days')
        isValidDate = False
elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
    if int(day) > 31:
        print('Day is out of range for month with 31 days')
        isValidDate = False
# For February
elif int(month) == 2 and ((int(year) % 4 == 0 or int(year) % 400 == 0) and not int(year) % 100 == 0):
    if (int(day)) > 29:
        print('Day is out of range in February')
        isValidDate = False
elif int(month) == 2 and not ((int(year) % 4 == 0 or int(year) % 400 == 0) and not int(year) % 100 == 0):
    if int(day) > 28:
        print('Day is out of range in February')
        isValidDate = False

if isValidDate:
    print('Date is valid')