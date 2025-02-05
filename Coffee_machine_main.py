from Coffee_machine_art import logo

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
}

# TODO 1: prompt user by asking 'what would you like?', print report (provide the current standing of resources)
# TODO 2: when the user order drink, should check whether if there is enough resources
# TODO 3: process coins
# TODO 4: check if the transaction is successful (check if it is enough coin, if too much coin then return change)
# TODO 5: make coffee (if there is sufficient resource and provided enough coin then, deduct ingredient from
#  machine resource


def check(order, items, menu):
    if order == 'espresso':
        if items["water"] >= menu[order]["ingredients"]["water"] and\
                items['coffee'] >= menu[order]["ingredients"]['coffee']:
            return True
        else:
            return False
    elif order == 'latte' or order == 'cappuccino':
        if items["water"] >= menu[order]["ingredients"]["water"] and\
                items['coffee'] >= menu[order]["ingredients"]['coffee'] and\
                items['milk'] >= menu[order]["ingredients"]["milk"]:
            return True
        else:
            return False
    elif order == 'report':
        return 'report'
    elif order == 'off':
        return 'off'


def resources_deduct(order):
    global resources, MENU
    if order == 'espresso':
        resources['water'] -= MENU[order]["ingredients"]["water"]
        resources['coffee'] -= MENU[order]["ingredients"]["coffee"]
    elif order == 'latte' or order == 'cappuccino':
        resources['water'] -= MENU[order]["ingredients"]["water"]
        resources['coffee'] -= MENU[order]["ingredients"]["coffee"]
        resources['milk'] -= MENU[order]["ingredients"]["milk"]


profit = 0
while True:
    print(logo)
    command = input("What would you like?(espresso/latte/cappuccino)☕️: ").lower()
    result = check(command, resources, MENU)

    if result == 'report':
        print(f"Resources Report:\n"
              f"Current Water level is {resources['water']}ml,\n"
              f"Milk level is {resources['milk']}ml,\n"
              f"Coffee level is {resources['coffee']}g and\n"
              f"Profit is ${profit}")
    elif result == 'off':
        print("The machine is under maintenance")
        break
    elif result:
        print("Please insert coin:")
        pennies = int(input("How many pennies?")) * 0.01
        nickles = int(input("How many nickles?")) * 0.05
        dimes = int(input("How many dimes?")) * 0.1
        quarters = int(input("How many quarters?")) * 0.25
        total = round(pennies + nickles + dimes + quarters, 2)

        if total < MENU[command]['cost']:
            print(f"Sorry. That is not enough money and refunded ${total}")
            break
        elif total > MENU[command]['cost']:
            print(f"You have a change of ${round(total - MENU[command]['cost'],2)}")
            profit += MENU[command]['cost']
            resources_deduct(command)
            print(f"Coffee Up, Enjoy your coffee")
        else:
            profit += MENU[command]['cost']
            resources_deduct(command)
            print(f"Coffee Up, Enjoy your coffee")
    else:
        print("Insufficient Ingredients")
        break
    
