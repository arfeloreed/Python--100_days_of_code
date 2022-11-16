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


def calculate_resources(original_resources, type_coffee):
    """Subtract the resources of the type of coffee to that of the original resources. Then prints the
        available resources.
    """
    original_resources["water"] -= type_coffee["water"]
    if "milk" in type_coffee:
        original_resources["milk"] -= type_coffee["milk"]
    original_resources["coffee"] -= type_coffee["coffee"]
    return original_resources


def can_make(original_resources, type_coffee):
    """Checks whether the available resources are enough to make a coffee ordered by the user."""
    make_coffee = True
    if type_coffee["water"] > original_resources["water"]:
        print("Sorry there is not enough water.")
        make_coffee = False
    if type_coffee["coffee"] > original_resources["coffee"]:
        print("Sorry there is not enough coffee.")
        make_coffee = False
    if "milk" in type_coffee:
        if type_coffee["milk"] > original_resources["milk"]:
            print("Sorry there is not enough milk.")
            make_coffee = False
    return make_coffee


def total_money_paid():
    """Total sum of the money paid by the user and returns the total money"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return (QUARTERS * quarters) + (DIMES * dimes) + (NICKLES * nickles) + (PENNIES * pennies)


def processing_coffee():
    """Main process of the coffee. It returns true if it can make the ordered coffee."""
    coffee_available = can_make(resources, MENU[user_order]["ingredients"])
    if coffee_available:
        total_money = total_money_paid()
        if total_money < MENU[user_order]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if total_money > MENU[user_order]["cost"]:
                change = round(total_money - MENU[user_order]["cost"], 2)
                print(f"Here is ${change} in change.")
            print(f"Here is your {user_order}. Enjoy.!")
            return True


def add_resources():
    """Refills the resources to full capacity"""
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    return resources


money = 0
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
while True:
    user_order = input("What would you like? (espresso,latte,cappuccino): ").lower()
    if user_order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user_order == "espresso":
        if processing_coffee():
            money += MENU[user_order]["cost"]
            resources = calculate_resources(resources, MENU[user_order]["ingredients"])
    elif user_order == "latte":
        if processing_coffee():
            money += MENU[user_order]["cost"]
            resources = calculate_resources(resources, MENU[user_order]["ingredients"])
    elif user_order == "cappuccino":
        if processing_coffee():
            money += MENU[user_order]["cost"]
            resources = calculate_resources(resources, MENU[user_order]["ingredients"])
    elif user_order == "refill":
        add_resources()
    elif user_order == "off":
        break
    else:
        print("Invalid input.")
