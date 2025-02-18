from turtle import Turtle, Screen
import random

is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)  # set the screen size
user_bet = screen.textinput(title='make your bet', prompt='which turtle will win the race? Enter a color:')
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
all_turtles = []  # a list of turtle objects

pos_y = 80

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=pos_y)  # if the turtle location is -250, it will be out of bound
    pos_y -= 30
    all_turtles.append(new_turtle)

# if user_bet:
#     is_race_on = True  # to prevent premature game start while user is still choosing turtle

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:  # any turtle that has x-cor more than 230, that is the winner and stop the race.
            is_race_on = False
            winning_turtle = turtle.pencolor()  # get the color of the winner to compare with user bet
            if winning_turtle == user_bet:
                print(f"You've won!, the winning turtle is {winning_turtle}")
            else:
                print(f"You've lost!, the winning turtle is {winning_turtle}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
