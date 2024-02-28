import time

logo = """         ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.xxxxx-'    __/ \__ |
                                                      """
print(logo)
print("Welcome to Treasure Island....")
print("Your Mission is to find the treasure...")

road = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' ")
if road == "left":
    time.sleep(2)
    lake = input(
        "You cam to lake. There is an island in the middle of the lake. "
        "Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if lake == "wait":
        time.sleep(2)
        iland = input(
            "You arrive at th island unharmed. There is a house with 3 doors. "
            "One red and yellow and one blue. Which cloud do you choose?")
        if iland == "yellow":
            time.sleep(1)
            print(
                "Yess $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ \n$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n YOU WON")
        else:
            time.sleep(2)
            print("Monster Hunted You! Game Over")
    else:
        print(" you drowned in to the see! Game Over!")
else:
    time.sleep(2)
    print("Wrong Turn!......Game Over")
