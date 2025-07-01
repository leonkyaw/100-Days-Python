from turtle import Turtle

SCORE_FONT = ("Courier", 15, "bold")


class HighScore(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-235, 280)
        self.color("white")
        self.high_score = self.get_high_score()
        self.write(f"High Score: {self.high_score}", align="center", font=SCORE_FONT)

    def get_high_score(self):
        with open('score.csv') as file:
            return int(file.read())
