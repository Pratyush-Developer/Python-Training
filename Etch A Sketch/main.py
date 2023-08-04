from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    tim.forward(10)


def counter():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.forward(10)


screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(clear, "c")
screen.onkey(clockwise, "a")
screen.onkey(counter, "d")


screen.exitonclick()
