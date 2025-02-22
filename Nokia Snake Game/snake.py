from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.snake_create()
        self.heading = self.segments[0]

    def snake_create(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start, stop, step
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # the segment go to the position to second segment
        self.heading.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color('burlywood2')
        turtle.goto(position)
        self.segments.append(turtle)

    def extend(self):
        """
        This function will add the new segment to the snake when the snake eat the food
        """
        self.add_segment(self.segments[-1].position())  # add the new segment into the current position of the segment


    def up(self):
        if self.heading.heading() != DOWN:  # if the current direction is up, can't move down
            self.heading.setheading(UP)

    def down(self):
        if self.heading.heading() != UP:
            self.heading.setheading(DOWN)

    def left(self):
        if self.heading.heading() != RIGHT:
            self.heading.setheading(LEFT)

    def right(self):
        if self.heading.heading() != LEFT:
            self.heading.setheading(RIGHT)
