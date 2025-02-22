from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')  # because Food class is inherit from turtle class, can use all methods straight away
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('DarkSeaGreen3')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x,y=random_y)
