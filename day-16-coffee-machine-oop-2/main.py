from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

MACHINE_RUNNING = True


def operating_machine():
    global MACHINE_RUNNING
    while MACHINE_RUNNING:
        choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

        if choice == "report":
            coffee_maker.report()
            money_machine.report()

        elif choice == "off":
            MACHINE_RUNNING = False


        elif choice == "espresso" or "latte" or "cappuccino":
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


operating_machine()