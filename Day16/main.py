from click import option
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_item = Menu()


is_on = True

while is_on:
    options: menu_item.get_items()
    choice = input(f"What would you like {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu_item.find_drink(choice)   
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

        



