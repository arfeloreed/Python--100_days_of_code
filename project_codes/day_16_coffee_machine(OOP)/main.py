from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee = Menu()
report = CoffeeMaker()
money = MoneyMachine()
while True:
    drink = input(f"What would you like? ({coffee.get_items()}): ")
    if drink == "report":
        report.report()
        money.report()
    elif drink == "off":
        break
    else:
        if report.is_resource_sufficient(coffee.find_drink(drink)):
            if money.make_payment(coffee.find_drink(drink).cost):
                report.make_coffee(coffee.find_drink(drink))
