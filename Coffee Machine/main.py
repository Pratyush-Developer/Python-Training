from Data import MENU
from Data import resources


def user_choice():
    user = input("What would you like? (espresso/latte/cappuccino): ")
    resource_check(user)


def resource_check(user):
    water_resource = resources.get("water")
    milk_resource = resources.get("milk")
    coffee_resource = resources.get("coffee")
    for x in MENU.keys():
        if user == x:
            water_menu = MENU.get(x).get("ingredients").get("water")
            milk_menu = MENU.get(x).get("ingredients").get("milk")
            coffee_menu = MENU.get(x).get("ingredients").get("coffee")
            if water_menu <= water_resource:
                if milk_menu <= milk_resource:
                    if coffee_menu <= coffee_resource:
                        drink(user)
                    else:
                        print("Sorry there is not enough coffee!!")
                        user_choice()
                else:
                    print("Sorry there is not enough milk!!")
                    user_choice()
            else:
                print("Sorry there is not enough water!!")
                user_choice()

    if user == "report":
        print("Water: ", resources["water"], "ml")
        print("Milk: ", resources["milk"], "ml")
        print("Coffee: ", resources["coffee"], "g")
        print("Money: $", resources["money"])
        user_choice()
    else:
        exit()


def drink(user):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    coffee_machine(quarters, dimes, nickles, pennies, user)


def coffee_machine(quarters, dimes, nickles, pennies, user):
    for x in MENU.keys():
        if user == x:
            price = MENU.get(x).get("cost")
            user_price = quarters + dimes + nickles + pennies
            if price <= user_price:
                change = round(user_price - price, 2)
                income = + price
                stock_water = resources.get("water") - MENU.get(x).get("ingredients").get("water")
                stock_milk = resources.get("milk") - MENU.get(x).get("ingredients").get("milk")
                stock_coffee = resources.get("coffee") - MENU.get(x).get("ingredients").get("coffee")
                resources.update({"water": stock_water, "milk": stock_milk, "coffee": stock_coffee})
                resources.update({"money": income})
                print(f"Here is ${change} in change.")
                print(f"Here is your {x}. Enjoy!!")
                user_choice()
            else:
                print("Sorry that's not enough money. Money refunded.")
                user_choice()


user_choice()
