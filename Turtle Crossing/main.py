import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Tutle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create()
    car_manager.car_move()

    # check for collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # the turtle is 20 x 20 pixel
            scoreboard.game_over()
            game_is_on = False

    # detect the crossing
    if player.is_at_finish_line():
        scoreboard.score_increase()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()
