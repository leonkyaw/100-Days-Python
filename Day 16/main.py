from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Assign object
making_coffee = CoffeeMaker()
money_machine = MoneyMachine()
menu_search = Menu()

menu_list = menu_search.get_items()

while True:
    order = input(f"What would you like?({menu_list}): ").lower()

    if order == "report":
        making_coffee.report()
        money_machine.report()
    elif order == "off":
        print("The machine is under maintenance")
        break
    else:
        drink = menu_search.find_drink(order)
        if making_coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):  # drink is the Menu Item object and they have 3 attributes (name, cost, ingredients)
            making_coffee.make_coffee(drink)
