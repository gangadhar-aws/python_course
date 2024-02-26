
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill ?  $"))
people = int(input("How many people to split the bill? "))
pr = int(input("What percentage tip would you like to give?  10, 12, or 15 ? "))
total_bill = bill + (bill/pr)
# total_bill = pr/100 * bill + bill
print(total_bill)
pay = round(total_bill/people,2)

print(f"Each Person should pay: ${pay}")
