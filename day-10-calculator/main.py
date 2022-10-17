from art import logo

print(logo)

#calculation function
def calculation(first_number, operator, second_number):
    """takes 2 numbers and an operator and calculates the mathematical result"""
    if operator == "*":
        result = first_number * second_number
    elif operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "/":
        result = first_number / second_number
    return float(result)

static_input = True
#inputs
first_number = float(input("What's the first number?: "))

while static_input == True:
    operator = input("""+
-
*
/
Pick an operator: """)
    second_number = float(input("What's the next number?: "))

    calculated_value = calculation(first_number, operator, second_number)
    print(f"{first_number} {operator} {second_number} = {calculated_value}")
    if input(f"Type 'y' to continue, calculating with {calculated_value}, or type 'n' to start new calculation: ").lower() == "y":
        first_number = calculated_value
    else:
        first_number = float(input("What's the first number?: "))



