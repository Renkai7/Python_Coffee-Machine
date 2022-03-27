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
    "milk": 100,
    "coffee": 100,
}


# TODO - Prompt user asking "What would you like? (espresso/latte/cappuccino):"
machine_status_on = True

while machine_status_on:
    user_input = input("What would you like?  (espresso/latte/cappuccino): ").lower()

    # TODO - Turn off Coffee machine by entering "off" to prompt
    if user_input == "off":
        machine_status_on = False

    # TODO - Print report
    if user_input == "report":
        print(resources)
    # TODO - Check resources sufficient

    #  check if user inputted a drink option

# TODO - Process coins

# TODO - Check transaction successful?

# TODO - Make Coffee
