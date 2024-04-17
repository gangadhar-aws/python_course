

user_input = input("Enter List of Numbers with Space").split()
my_list = [int(num) for num in user_input]

# sum of numbers
total = sum(my_list)
print(total)