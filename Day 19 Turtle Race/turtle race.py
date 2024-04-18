from turtle import Turtle, Screen
import random

screen = Screen()

# Setting screen Setup of Turtle Game
screen.setup(width=600, height=400)

#taking input from user which turtle win
bet=screen.textinput(title="Pick the Color", prompt="Witch Color Turtle Win")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
b=-150

for i in range(6):
    name=colors[i]
    name = Turtle(shape="turtle")
    name.color(colors[i])
    name.penup()
    b = b+50
    name.goto(x=-270, y=b)
    all_turtles.append(name)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            winnig_color = turtle.pencolor()
            if winnig_color == bet:
                print("You Won The Race!")
                print(winnig_color)
                is_race_on = False
            else:
                print("Oh!! You Lost The Race")
                print(winnig_color)
                is_race_on = False
        distance = random.randint(0,10)
        turtle.forward(distance=distance)









screen.exitonclick()