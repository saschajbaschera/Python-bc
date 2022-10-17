#This solution is created following the tuition video

from art import logo

#calculator


#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

#creating a dict
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    print("Welcome to the worlds best Calculator >.>")
    num1 = float(input("What's the first number?: "))
    loop = True
    while loop == True:

        for item in operations:
            print(item)
        
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the next number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")


        if input(f"Type 'y' to continue, calculating with {answer}, or type 'n' to start a new calculation ") == "y":
            num1 = answer
        else:
            calculator()

calculator()