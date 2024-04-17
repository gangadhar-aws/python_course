from turtle import Turtle, Screen


screen = Screen()

# Setting screen Setup of Turtle Game
screen.setup(width=600, height=400)

#taking input from user which turtle win
bet=screen.textinput(title="Pick the Color", prompt="Witch Color Turtle Win")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

 
b=-150
for i in range(6):
    name=colors[i]
    name = Turtle(shape="turtle")
    name.color(colors[i])
    name.penup()
    b = b+50
    name.goto(x=-270, y=b)











screen.exitonclick()