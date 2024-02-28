import time

print("The Love Calculator is calculating your score...")
name1 = input("What is your name ? ").lower()
name2 = input("What is their name ? ").lower()

full_name = name1 + name2
true = full_name.count("t") + full_name.count("r") + full_name.count("u") + full_name.count("e")
love = full_name.count("l") + full_name.count("0") + full_name.count("v") + full_name.count("e")
score = int(str(true) + str(love))

if score < 10 or score > 90:
    print("The Love Calculator is calculating your score...")
    time.sleep(3)
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print("The Love Calculator is calculating your score...")
    time.sleep(3)
    print(f"Your score is {score}, you are alright together.")
else:
    print("The Love Calculator is calculating your score...")
    time.sleep(3)
    print(f"Your score is {score}.")
