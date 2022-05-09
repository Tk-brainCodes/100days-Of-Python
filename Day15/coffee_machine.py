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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resourse_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not {item}")
            return False
    return True 

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins. ")
    total = int(input("How many quaters:  ")) * 0.25
    total = int(input("How many dimes:  ")) * 0.1
    total = int(input("How many nickels:  ")) * 0.05
    total += int(input("How many pennies:  ")) * 0.01
    return total

def is_transaction_scuccessful(money_received, drinks_cost):
    if money_received >= drinks_cost:
        change = round(money_received, 2)
        print(f"Here is ${change} in change")
        global profit 
        profit += drinks_cost
        return True
    else:
        print("Sorry thats not enough money. Money refunded")


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your coffeee! {drink_name}")    


profit = 0

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml,")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]  
        if is_resourse_sufficient(drink["ingredients"]):
            paymemnt = process_coins()
            if is_transaction_scuccessful(paymemnt, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



 