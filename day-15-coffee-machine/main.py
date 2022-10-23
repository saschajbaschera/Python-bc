from resources import MENU, resources


# write a function to check if there are enough resources for the inputting beverage
def check_resources(beverage):
    low = []
    if beverage == "espresso":
        if resources["water"] - MENU[beverage]["ingredients"]["water"] >= 0:
            if resources["coffee"] - MENU[beverage]["ingredients"]["coffee"] >= 0:
                return True
        else:
            return False
    else:
        if resources["water"] - MENU[beverage]["ingredients"]["water"] >= 0:
            if resources["coffee"] - MENU[beverage]["ingredients"]["coffee"] >= 0:
                if resources["milk"] - MENU[beverage]["ingredients"]["milk"] >= 0:
                    return True
        else:
            return False


# Create a function to calculate the amount that was inputting in coins
def calculate_amount(quarters, dimes, nickles, pennies):
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total


# Create a function which deducts the needed ingredients of the beverage from the machines resources
def deduct_and_deposit(beverage):
    resources["money"] = resources["money"] + MENU[beverage]["cost"]
    if beverage == "espresso":
        resources["water"] = resources["water"] - MENU[beverage]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[beverage]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - MENU[beverage]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[beverage]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU[beverage]["ingredients"]["milk"]


def running_low(beverage):
    low = []
    if beverage == "espresso":
        if resources["water"] - MENU[beverage]["ingredients"]["water"] <= 0:
            low.append("water")
        if resources["coffee"] - MENU[beverage]["ingredients"]["coffee"] <= 0:
            low.append("coffee")
    else:
        if resources["water"] - MENU[beverage]["ingredients"]["water"] <= 0:
            low.append("water")
        if resources["coffee"] - MENU[beverage]["ingredients"]["coffee"] <= 0:
            low.append("coffee")
        if resources["milk"] - MENU[beverage]["ingredients"]["milk"] <= 0:
            low.append("milk")
    return low


MACHINE_RUNNING = True


def machine():
    global MACHINE_RUNNING
    while MACHINE_RUNNING:
        # ask what the user wants to drink, espresso, latte or cappuccino
        choice = input("What would you like? ").lower()

        # with "report" the user can extract how many resources there are in the coffee machine
        if choice == "report":
            print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}""")

        if choice == "off":
            print("Machine is shutting down now.... beep beep off")
            MACHINE_RUNNING = False
            return

        if choice != "report" and choice != "off":

            # based on the chosen beverage it checks if the machine has enough resources
            enough_resources = check_resources(choice)

            # if there are enough resources it's asking to insert coins
            if enough_resources:
                quarters = int(input("Please input coins.\nHow many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))

                change = float("{:.3f}".format(calculate_amount(quarters, dimes, nickles, pennies) - MENU[choice]["cost"]))
                # if the user inserted enough money it returns he change amount in $
                if change >= 0:
                    print(f"Here is ${change} in change.\nHere is your {choice}! Enjoy!")
                    deduct_and_deposit(choice)

                else:
                    print("Not enough funds, here is your money back!")
            else:
                print(f"There are not enough resources, please refill {running_low(choice)}")
                return


machine()




