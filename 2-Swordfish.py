while True:
    print("Who are you?")
    name = input()

    if name == "Joe":
        print("Hello Joe, what is the password?")
        password = input()

        while password != "swordfish":
            print("Wrong password, try again")
            password = input()

        print("Access granted")
        break
