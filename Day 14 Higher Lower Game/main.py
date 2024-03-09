from art import logo, vs
from gamedata import data
import random


question_A = random.choice(data)
question_B = random.choice(data)
question_c = None
# print(question_B)
# print(question_A)
score = 0

game_on = True
while game_on:
    print(logo)
    if score > 0:
        print("You're right! Current score: ", score)

    print(f"Compare A: {question_A["name"]}, a {question_A["description"]}, from {question_A["country"]}.")
    print(vs)
    print(f"Against B: {question_B["name"]}, a {question_B["description"]}, from {question_B["country"]}.")
    guess = input("Who has more followers ? Type 'A' or 'B' :").lower()

    if question_A["follower_count"] > question_B["follower_count"] and guess == 'a':
        print("You Win")
        question_A = question_B
        question_B = random.choice(data)
        score +=1
    elif question_B["follower_count"] > question_A["follower_count"] and guess == 'b':
        print("you Win")
        question_A = question_B
        question_B = random.choice(data)
        score +=1
    else:
        print("You Lose")
        game_on = False
        print("You are Total Score : ", score)
