MENU = {
    "coffee": {
        "ingredients": {
            "water": 50,
            "coffee": 15,
            "milk": 0,
        },
        "cost": 10,
    },
    "tea": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 15,
    },
    "mc": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 20,
    }
}

resources = {
    "water": 300,  #300,
    "milk": 200,
    "coffee": 200,
}
money = 0


# TODO: 1. Print report
# TODO: 2. Check resources sufficient? before asking money from user
# TODO: 3. Process coins if enough or not check, and calculate how much money we entered tell the user if less amount inserted
# TODO: 4. check translation successful
# TODO: 5. make coffe.
import time

def print_report():
    print(
        f"Water: {resources["water"]}ml \n Milk: {resources["milk"]}ml \n Coffee:{resources["coffee"]}g \n Money: ${money}")

def check_resource(item):
    if resources["water"] > int(MENU[item]["ingredients"]["water"]):
        if resources["milk"] > MENU[item]["ingredients"]["milk"]:
            if resources["coffee"] > MENU[item]["ingredients"]["coffee"]:
                return item
            else:
                return "Not Enough Coffee"
        else:
            return "Not Enough Milk"
    else:
        return "Not Enough Water"


def process_coins():
    rupees, five, ten, fifty = 0,0,0,0
    rupees = int(input("How Many Rupees ?:"))
    five = int(input("How Many five Rupees ?:"))
    ten = int(input("How Many Ten Rupees ?:"))
    fifty = int(input("How Many Fifty Rupees ?:"))
    total = rupees+five*5+ten*10+fifty*50
    return total
def prepare_drink(item):
    resources["water"] -= MENU[item]["ingredients"]["water"]
    resources["milk"] -= MENU[item]["ingredients"]["milk"]
    resources["coffee"] -= MENU[item]["ingredients"]["coffee"]

machine_off = True

while machine_off:
    my_list = ["coffee", "tea", "mc"]
    user_entry = input("What would you Like ? (coffee/tea/milk_coffe -mc) :").lower()
    if user_entry == "report":
        print("Printing Report...")
        time.sleep(2)
        print_report()
    elif user_entry in my_list:
        machine_message = check_resource(user_entry)
        if machine_message == user_entry:
            customer_money = process_coins()
            if customer_money >= MENU[user_entry]["cost"]:
                prepare_drink(user_entry)
                money += MENU[user_entry]["cost"]
                print(f"Enjoy Your {user_entry}")
                print(f"Please Collect your Balance Amount ${customer_money-MENU[user_entry]["cost"]}")
            else:
                print(f"Not Enough Money please collect your money {customer_money}")
        else:
            print(machine_message)
    elif user_entry == "off":
        machine_off = False
    else:
        print("Wrong Button Pressed Try Again!")
