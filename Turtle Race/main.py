from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_cor = -100
is_race_on = False
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index - 1])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cor)
    y_cor += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for x in all_turtles:
        if x.xcor() >= 230:
            is_race_on = False
            winning_color = x.pencolor()
            if winning_color == user_bet:
                print(f"You won!! The {winning_color} turtle in the winner!")
            else:
                print(f"You lost!! The {winning_color} turtle in the winner!")
        motion = random.randint(0, 10)
        x.forward(motion)


screen.exitonclick()
