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

profit = 0

# TODO - Check resources sufficient

def is_enough_resource(drink_ingredients):
    for items in drink_ingredients:
        if drink_ingredients[items] > resources[items]:
            print(f"Not enough {items}")
            return False
    return True


# TODO - Process coins
def process_coins():
    print("Please insert coins.")

    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .10
    total += int(input("How many nickles?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total

# TODO - Check transaction successful?
def is_transaction_successful():
    if user_total > drink["cost"]:
        return True
    else:
        return False
# TODO - Make Coffee
def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

# TODO - Prompt user asking "What would you like? (espresso/latte/cappuccino):"
machine_status_on = True

while machine_status_on:
    user_input = input("What would you like?  (espresso/latte/cappuccino): ").lower()

    # TODO - Turn off Coffee machine by entering "off" to prompt
    if user_input == "off":
        machine_status_on = False

    # TODO - Print report
    elif user_input == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if is_enough_resource(drink["ingredients"]):
            print("Proceed to payment.")
            user_total = round(process_coins(), 2)
            if is_transaction_successful():
                print("You have enough money.")
                profit += user_total
                print(profit)
                if user_total > drink["cost"]:
                    user_overpayment = round(user_total - drink["cost"], 2)
                    profit = profit - user_overpayment
                    print(f"You overpaid. Here is your change: ${user_overpayment}")
                    print(f"New profit {profit}")
                    make_coffee(drink["ingredients"])
            else:
                print("Not enough money.")
        else:
            print("Cancel transaction.")



