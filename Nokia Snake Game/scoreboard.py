from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 25, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()  # have to clear what is previously on the screen, or else it will just print on top
        self.update_score()
