from turtle import Turtle

LEVEL_FONT = ("Courier", 15, "bold")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: 0", align="center", font=LEVEL_FONT)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=LEVEL_FONT)

    def level_up(self):
        self.level += 1
        self.update_level()
