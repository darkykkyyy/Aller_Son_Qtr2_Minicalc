
def getValues():
    firstnum = float(input("Enter the first number: "))
    secondnum = float(input("Enter the second number: "))
    return firstnum, secondnum


def calculate(firstnum, secondnum, operation):
    if operation == 1:
        return firstnum + secondnum
    elif operation == 2:
        return firstnum - secondnum
    elif operation == 3:
        return firstnum * secondnum
    elif operation == 4:
        if secondnum == 0:
            return "Error: Division by zero is not allowed."
        else:
            return firstnum / secondnum
    elif operation == 5:
        print("You thought you could break the code? Well, you can't!")
        return "You suck at trying to break the code. Please try again."
    else:
        return "Invalid operation selected."


firstnum, secondnum = getValues()

operation = int(input(
    "Enter the operation you want to perform "
    "(1 - addition, 2 - subtraction, 3 - multiplication, 4 - division): "
))

if operation < 1 or operation > 4:
    print("Invalid operation selected. Please choose a number between 1 and 4.")
else:
    result = calculate(firstnum, secondnum, operation)

    input("Press Enter to see the result...")
    input("Press again :)")
    input("Aww, you pressed it again! Good boy. Now, press Enter one last time!")
    input("Press Enter YET AGAIN :) to see the result...")

    print(result)