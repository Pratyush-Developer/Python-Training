from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.pencolor("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.write(f"Score:{self.count} High Score:{self.high_score}", False, align="center", font=("Aerial", 12, "normal"))

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.count = 0
        self.score_refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!!", False, align="center", font=("Aerial", 12, "normal"))

    def increase_score(self):
        self.count += 1
        self.score_refresh()
