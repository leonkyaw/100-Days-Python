from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", 'white']
ROW_BAR = 5
STARTING_POINT_X = -270
STARTING_POINT_Y = 250


class Bar:

    def __init__(self):
        self.bars = []
        self.create()

    def create(self):
        for row in range(ROW_BAR):
            global STARTING_POINT_X, STARTING_POINT_Y
            fit = True
            starting_point = STARTING_POINT_X
            while fit:
                bar = Turtle('square')
                bar.penup()
                bar.shapesize(stretch_wid=1, stretch_len=3)
                bar.goto(starting_point, STARTING_POINT_Y)
                bar.color(random.choice(COLORS))
                self.bars.append(bar)

                starting_point += 63

                if starting_point >= 265:
                    STARTING_POINT_Y -= 24
                    if row % 2 == 0:
                        STARTING_POINT_X -= 10
                    else:
                        STARTING_POINT_X += 10
                    fit = False

    def bar_reset(self):
        global STARTING_POINT_X, STARTING_POINT_Y
        STARTING_POINT_X = -270
        STARTING_POINT_Y = 250
        self.create()
