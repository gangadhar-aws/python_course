import random

print("Welcome to the Password Generator! ")
print("------------------------------------")
l = int(input("How many letters would you like in your password? \n"))
s = int(input("How many symbols would you like? \n"))
n = int(input("How many numbers would you like? \n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

word = [random.choice(letters) for i in range(l)]
num = [random.choice(numbers) for j in range(s)]
sym = [random.choice(symbols) for k in range(n)]
temp_pass = word+num+sym
random.shuffle(temp_pass)
password = ''.join(temp_pass)
print("Your Final Password is : ", password)




