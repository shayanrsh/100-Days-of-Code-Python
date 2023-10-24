from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_things = MoneyMachine()
coffee_maker = CoffeeMaker()

should_continue = True

while should_continue:
    user_input = input(f"What would you like? {menu.get_items()}:")
    if user_input == "off":
        print("Turning off the machine.")
        should_continue = False
    elif user_input == "report":
        coffee_maker.report()
        money_things.report()
    else:
        order = menu.find_drink(user_input)
        cost = menu.find_drink(user_input).cost
        if coffee_maker.is_resource_sufficient(order):
            if money_things.make_payment(cost):
                coffee_maker.make_coffee(order)
