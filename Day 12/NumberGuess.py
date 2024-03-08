import random


lives =  0
number = random.randint(1,100)


level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == 'easy':
    lives = 8
else:
    lives = 5

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess : "))
    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    elif guess == number:
        print("You Won The game")
    lives -= 1


print("Correct Number is ", number)