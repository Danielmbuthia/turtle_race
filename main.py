from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = -70
all_turtle = []
for color in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[color])
    tim.penup()
    tim.goto(x=-230, y=y)
    y += 30
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won the bet")
            else:
                print(f"You lost. The winning turtle was {turtle.pencolor()}")
        race_distance = random.randint(0, 10)
        turtle.forward(race_distance)

screen.exitonclick()
