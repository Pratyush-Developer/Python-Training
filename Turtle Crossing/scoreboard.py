from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 1
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)
        self.level_refresh()

    def level_refresh(self):
        self.clear()
        self.write(f"Level:{self.count}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!", align="center", font=FONT)

    def increase_level(self):
        self.count += 1
        self.level_refresh()
