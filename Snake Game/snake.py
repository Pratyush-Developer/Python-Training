from turtle import Turtle


POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_snake(self.turtles[-1].position())

    def move(self):
        for x in range(len(self.turtles) - 1, 0, -1):
            xcor = self.turtles[x - 1].xcor()
            ycor = self.turtles[x - 1].ycor()
            self.turtles[x].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for tim in self.turtles:
            tim.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]
