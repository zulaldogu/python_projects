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

machine = True
money = 0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def espresso():
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
        cost = MENU["espresso"]["cost"]
        is_payment_successful = process_coins(cost)
        if is_payment_successful == True:
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    else:
        print("Sorry, there is not enough resources left.")


def latte():
    if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
        cost = MENU["latte"]["cost"]
        is_payment_successful = process_coins(cost)
        if is_payment_successful == True:
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    else:
        print("Sorry, there is not enough resources left.")


def cappuccino():
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
        cost = MENU["cappuccino"]["cost"]
        is_payment_successful = process_coins(cost)
        if is_payment_successful == True:
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    else:
        print("Sorry, there is not enough resources left.")


def process_coins(cost):
    global money
    print("Please insert coins!")
    penny = int(input("Penny: "))
    nickle = int(input("Nickle: "))
    dime = int(input("Dime: "))
    quarter = int(input("Quarter: "))
    value = penny * 0.01 + nickle * 0.05 + dime * 0.10 + quarter * 0.25
    if value >= cost:
        money += cost
        change = round(value - cost, 2)
        print(f"Here is your change: ${change}")
        print(f"Here is your {coffee}. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


while (machine):
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "off":
        machine = False
    elif coffee == "report":
        report()
    elif coffee == "espresso":
        espresso()
    elif coffee == "latte":
        latte()
    elif coffee == "cappuccino":
        cappuccino()
