#TODO:2.check if all the resources are sufficient to make drink order

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

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough

def process_coins():
    """total calculated from coins inserted"""
    print("please insert coins")
    total = float(input("how many quarters?")) * 0.25
    total += float(input("how many dimes?")) * 0.1
    total += float(input("how many nickel?")) * 0.05
    total += float(input("how many pennies?")) * 0.01
    return float(total)

def is_transaction_successful(money_received,drink_cost):
    """return true when payment accepted or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost)
        print(f"here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money,your money is refunded")
        return False

def make_coffee(drink_name,order_ingredient):
    "deduct the required ingredients from the resources"
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"here is your {drink_name}☕")


is_on = True
while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:$ {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment,drink["cost"])
            make_coffee(choice,drink["ingredients"])
