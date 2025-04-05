from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 25, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save()
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()  # have to clear what is previously on the screen, or else it will just print on top
        self.update_score()

    # Managing High Score
    def save(self):
        with open("data.txt", mode='w') as file:
            file.write(str(self.high_score))

    def get_high_score(self):
        with open('data.txt') as file:
            return int(file.read())
