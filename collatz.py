def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


print("Enter number:")
a = input()
try:
    while True:
        print(collatz(int(a)))
        a = collatz(int(a))
        if a == 1:
            break
except ValueError:
    print("Input error, must be integer")
