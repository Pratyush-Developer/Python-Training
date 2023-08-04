import colorgram

# colors = colorgram.extract("image.jpg", 25)
#
# n = len(colors)
# extract = []
# for x in range(0, n - 1):
#     color = colors[x]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     extract.append(color_tuple)
#
# print(extract)
import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.colormode(255)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
              (172, 153, 159), (212, 183, 177)]
tim.speed("fast")


def random_color():
    color = random.choice(color_list)
    return color


tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)


def painting():
    for z in range(1, 11):
        tim.dot(20, random_color())
        tim.penup()
        tim.forward(50)
        if z == 10:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)
            painting()


painting()

screen.exitonclick()
