def commaCode(inputList):
    if len(inputList) != 0:
        for i in range(len(inputList)-1):
            print (inputList[i], end=", ")
        print("and " + inputList[-1])

spam = ["apples", "bananas", "tofu", "cats"]
tufu = []
commaCode(spam)
commaCode(tufu)
