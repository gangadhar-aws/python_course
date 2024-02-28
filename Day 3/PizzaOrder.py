print("Thank you for choosing Python Pizza Deliveries!")
size = input(" What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N")
bill = 0
if extra_cheese.lower() == "y":
    bill += 1

if size.lower() == "s":
    bill += 15
    if add_pepperoni.lower() == "y":
        bill += 2
elif size.lower() == "m":
    bill += 20
    if add_pepperoni.lower() == "y":
        bill += 3
elif size.lower() == "l":
    bill += 25
    if add_pepperoni.lower() == "y":
        bill += 3
else:
    print("Wrong Pizza Size Selection Try again! ")

print(f"Thank you for choosing Pizza Hut \n Your Final Bill is : {bill}")