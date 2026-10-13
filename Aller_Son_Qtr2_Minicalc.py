firstnum = float(input("Enter the first number: "))
secondnum = float(input("Enter the second number: "))



operation=int(input("Enter the operation you want to perform (1 - addition, 2 - subtraction, 3 - multiplication, 4 - division): "))

if operation < 1 or operation > 5:
    print("Invalid operation selected. Please choose a number between 1 and 4.")

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
            print("you thought you could break the code? well, you can't. You have to choose between 1-4. Now, please try again.")
            result = ("You suck at trying to break the code. Please try again.")
            return result
    else:
        return "Invalid operation selected."
    
result = calculate(firstnum, secondnum, operation)
delay = input("Press Enter to see the result...")
delay = input("press again :)")
delay = input("Aww, you pressed it again! Good boy. Now, press Enter one last time to see the result...")
freeze = input("Press Enter YET AGAIN :) to see the result...")
print(result)
