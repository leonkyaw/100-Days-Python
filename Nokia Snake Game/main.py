from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # turn off the animation
game_is_on = True

# screen.update()  # all the square blocks will show instantly without showing the animation of creating one by one
snake = Snake()  # this line will create the snake
food = Food()   # this will create the food
score = Score()

# Key stroke binding
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()  # the snake won't be shown on screen until the first time this code is executed.
    time.sleep(0.1)  # one-second delay after each segment moved.
    snake.move()

    # Detect collision with foods
    if snake.heading.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if abs(snake.heading.xcor()) > 290 or abs(snake.heading.ycor()) > 290:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    # if head is collide with any segment in the tail:
        # GAME OVER
    # first way to check tail connection
    # for segment in snake.segments:
    # the first segment is the head, and it will be game over as it equal to snake head
    #     if segment == snake.heading:  # check if the segment is the snake head, if yes then do nothing.
    #         pass
    for segment in snake.segments[1:]:  # use slicing
        if snake.heading.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
