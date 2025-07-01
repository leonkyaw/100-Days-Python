from turtle import Turtle
import csv
GAME_OVER_FONT = ("Courier", 25, "normal")
SCORE_FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(240, 280)
        self.color("white")
        self.write(f"Score: 0", align="center", font=SCORE_FONT)
        self.score = 0
        self.high_score = self.get_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=SCORE_FONT)

    def score_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align='center', font=GAME_OVER_FONT)

    def save(self):
        if self.score > self.high_score:
            with open('score.csv', 'w') as file:
                file.write(str(self.score))

    def get_high_score(self):
        try:
            with open('score.csv') as file:
                return int(file.read())
        except FileNotFoundError:
            with open('score.csv', 'w') as file:
                file.write(str(0))
