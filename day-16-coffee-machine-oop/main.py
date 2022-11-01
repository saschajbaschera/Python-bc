from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MACHINE_RUNNING = True
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while MACHINE_RUNNING:
    choice = input(f"What would you like? ({menu.get_items()})").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        print("Machine is shutting down... beep.. beep.. bob")
        MACHINE_RUNNING = False

    elif choice not in menu.get_items():
        print("Your item is not on the menu")

    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)



