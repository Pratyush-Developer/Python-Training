from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()

# Different Shapes
# direction = [0, 90, 180, 270]

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")
# def shape(num_sides):
#     degree = 360/num_sides
#     for z in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(degree)
#
#
# for x in range(3, 11):
#     shape(x)

screen.colormode(255)

# Random Walk


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# count = 0
# while count < 500:
#     count += 1
#     timmy_the_turtle.pensize(10)
#     timmy_the_turtle.speed(0)
#     timmy_the_turtle.pencolor(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(direction))

# Draw a Spirograph
screen.bgcolor("black")
timmy_the_turtle.speed(0)


def draw_spirograph(size_of_gap):
    for x in range(int(360 / size_of_gap)):
        timmy_the_turtle.circle(80)
        timmy_the_turtle.pencolor(random_color())
        current_heading = timmy_the_turtle.heading()
        timmy_the_turtle.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen.exitonclick()



