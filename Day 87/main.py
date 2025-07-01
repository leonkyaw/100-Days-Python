from turtle import Screen
from target import Bar
from player_bar import Player
from ball import Ball
from scoreboard import Scoreboard
from level import Level
from highscore import HighScore
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Breakout Game')
game_is_on = True
screen.tracer(0)

# create object
target = Bar()
player = Player((0, -250))
ball = Ball()
scoreboard = Scoreboard()
level = Level()
highscore = HighScore()

screen.listen()
screen.onkey(fun=player.go_left, key='Left')
screen.onkey(fun=player.go_right, key='Right')


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collisions
    for bar in target.bars:
        if ball.distance(bar) < 35 and ball.distance(bar) < 35:
            target.bars.remove(bar)
            bar.hideturtle()
            scoreboard.score_up()
            ball.bounce_x()

    # Collisions with wall
    if abs(ball.xcor()) > 275:
        ball.bounce_x()

    if abs(ball.ycor()) > 275:
        ball.bounce_y()

    # Collision with paddle
    if ball.distance(player) < 40 and ball.ycor() > -275:
        ball.bounce_y()

    # Game over
    if ball.ycor() < -275:
        scoreboard.game_over()
        scoreboard.save()
        game_is_on = False

    # Level up
    if len(target.bars) == 0:
        ball.reset_position()
        target.bar_reset()
        level.level_up()

screen.exitonclick()
