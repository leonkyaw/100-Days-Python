from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.hideturtle()
        self.penup()
        self.goto(-240, 250)
        self.write(arg=f"LEVEL:{self.score}", align='center', font=FONT)

    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(arg=f"LEVEL:{self.score}", align='center', font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align='center', font=FONT)

