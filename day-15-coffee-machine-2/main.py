MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_resources():
    print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}""")


def check_resources(choice):
    """Returns true if there are enough resources to produce the users choice of beverage. Returns False if not."""
    if choice == "espresso":
        if resources["water"] - MENU[choice]["ingredients"]["water"] >= 0:
            if resources["coffee"] - MENU[choice]["ingredients"]["coffee"] >= 0:
                return True
        else:
            return False

    else:
        if resources["water"] - MENU[choice]["ingredients"]["water"] >= 0:
            if resources["coffee"] - MENU[choice]["ingredients"]["coffee"] >= 0:
                if resources["milk"] - MENU[choice]["ingredients"]["milk"] >= 0:
                    return True
        else:
            return False


def low_resources(choice):
    """Adds the resources which are low to make the users choice to a list and returns list."""
    low = []
    if choice == "espresso":
        if resources["water"] - MENU[choice]["ingredients"]["water"] < 0:
            low.append("water")
        if resources["coffee"] - MENU[choice]["ingredients"]["coffee"] < 0:
            low.append("coffee")

    else:
        if resources["water"] - MENU[choice]["ingredients"]["water"] < 0:
            low.append("water")
        if resources["coffee"] - MENU[choice]["ingredients"]["coffee"] < 0:
            low.append("coffee")
        if resources["milk"] - MENU[choice]["ingredients"]["milk"] < 0:
            low.append("milk")

    return low


def handle_money(choice):
    """If enough money, adds the money to the resources and handles change and returns True."""
    print("Please insert coins!")
    quarters = float(input("How many quarters?\n"))
    dimes = float(input("How many dimes?\n"))
    nickles = float(input("How many nickles?\n"))
    pennies = float(input("How many pennies?\n"))

    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if choice == "espresso":
        if total < MENU[choice]["cost"]:
            print(f"Sorry ${total: .2f} is not enough, an espresso costs ${1.50}. Here is your money back.")
        else:
            resources["money"] += MENU[choice]["cost"]
            if total > MENU[choice]["cost"]:
                print(f"Here is ${total - 1.5: .2f} dollars in change")
            return True

    elif choice == "latte":
        if total < MENU[choice]["cost"]:
            print(f"Sorry ${total} is not enough, a latte costs $2.50. Here is your money back.")
        else:
            resources["money"] += MENU[choice]["cost"]
            if total > MENU[choice]["cost"]:
                print(f"Here is ${total - 2.5: .2f} dollars in change")
            return True

    elif choice == "cappuccino":
        if total < MENU[choice]["cost"]:
            print(f"Sorry ${total} is not enough, a cappuccino costs $3.00. Here is your money back.")
        else:
            resources["money"] += MENU[choice]["cost"]
            if total > MENU[choice]["cost"]:
                print(f"Here is ${total - 2.5: .2f} dollars in change")
            return True

    else:
        return False


def make_coffee(choice):
    if choice == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18

    elif choice == "latte":
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150

    elif choice == "cappuccino":
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100


MACHINE_RUNNING = True


def machine_runs():
    global MACHINE_RUNNING
    while MACHINE_RUNNING:
        choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

        if choice == "report":
            print_resources()

        elif choice == "off":
            print("Machine is turning off beep boop")
            MACHINE_RUNNING = False

        elif choice == "espresso" or "latte" or "cappuccino":
            if check_resources(choice):
                if handle_money(choice):
                    make_coffee(choice)
                    print(f"Here is your {choice}. ENJOY!")
                else:
                    print("There has been an issue with handling the money!")
            else:
                print(f"Sorry there is not enough {', '.join(low_resources(choice))}.")


machine_runs()
