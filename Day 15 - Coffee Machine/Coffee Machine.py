from menu import MENU, resources

should_continue = True
profit = 0


def ask_user(ask_user_input, ask_MENU):
    """a. Check the user’s input to decide what to do next.
    b. The prompt should show every time action has completed, e.g. once the drink is
    dispensed. The prompt should show again to serve the next customer."""
    if ask_user_input == "espresso":
        need_water = ask_MENU["espresso"]["ingredients"]["water"]
        need_milk = 0
        need_coffee = ask_MENU["espresso"]["ingredients"]["coffee"]
        need_money = ask_MENU["espresso"]["cost"]
    else:
        need_water = ask_MENU[ask_user_input]["ingredients"]["water"]
        need_milk = ask_MENU[ask_user_input]["ingredients"]["milk"]
        need_coffee = ask_MENU[ask_user_input]["ingredients"]["coffee"]
        need_money = ask_MENU[ask_user_input]["cost"]
    return need_water, need_milk, need_coffee, need_money


def turn_off(user_input_off):
    """a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    the machine. Your code should end execution when this happens."""
    global should_continue
    if user_input_off == "off":
        should_continue = False
    return should_continue


def print_report(report_water, report_milk, report_coffee, report_money):
    """When the user enters “report” to the prompt, a report should be generated that shows
    the current resource values"""
    return f"Water: {report_water}ml\nMilk: {report_milk}ml\nCoffee: {report_coffee}g\nMoney: ${report_money}"


def check_resources(water_amount, milk_amount, coffee_amount):
    """a. When the user chooses a drink, the program should check if there are enough
    resources to make that drink.
    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    not continue to make the drink but print: “ Sorry there is not enough water. ”
    c. The same should happen if another resource is depleted, e.g. milk or coffee."""
    if resources["water"] < water_amount:
        return "Sorry there is not enough water."
    elif resources["milk"] < milk_amount:
        return "Sorry there is not enough milk."
    elif resources["coffee"] < coffee_amount:
        return "Sorry there is not enough coffee."
    else:
        return "enough"


def process_coins():
    """a. If there are sufficient resources to make the drink selected, then the program should
    prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def check_transaction(check_money_amount, check_need_money):
    """a. Check that the user has inserted enough money to purchase the drink they selected.
    E.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    program should say “ Sorry that's not enough money. Money refunded. ”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the
    machine as the profit and this will be reflected the next time “report” is triggered. E.g.
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
    c. If the user has inserted too much money, the machine should offer change.
    E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
    places."""
    if check_money_amount < check_need_money:
        return False, "Sorry that's not enough money. Money refunded."
    elif check_money_amount >= check_need_money:
        return True, f"Here is ${round(check_money_amount - check_need_money, 2)} in change."


def make_coffee(water, milk, coffee, user_input):
    """a. If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink should be deducted from the
    coffee machine resources.
    E.g. report before purchasing latte:
    Water: 300ml
    Milk: 200ml
    Coffee: 100g
    Money: $0
    Report after purchasing latte:
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    latte was their choice of drink."""

    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee
    global profit
    profit += MENU[user_input]["cost"]
    return f"Here is your {user_input}. ☕ Enjoy!", resources


def machine():
    water, milk, coffee, money = ask_user(user_input, MENU)
    if check_resources(water, milk, coffee) == "enough":
        user_money_input = process_coins()
        if not check_transaction(user_money_input, money)[0]:
            print(check_transaction(user_money_input, money)[1])
        else:
            print(check_transaction(user_money_input, money)[1])
            print(make_coffee(water, milk, coffee, user_input)[0])
    else:
        print(check_resources(water, milk, coffee))


while should_continue:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if turn_off(user_input):
        if user_input == "report":
            print(print_report(resources["water"], resources["milk"], resources["coffee"], profit))
        else:
            machine()
    else:
        print("Turning off the machine.")
