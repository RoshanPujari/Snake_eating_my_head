from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey")
screen.tracer(0)
# TODO 1: Create a snake body.
starting_position = [(0, 0), (-20, 0), (-40, 0)]

snakenew = Snake()

#listen to the key pressed
screen.listen()

# Keys to control the snake
screen.onkey(snakenew.up, "Up")
screen.onkey(snakenew.down, "Down")
screen.onkey(snakenew.left, "Left")
screen.onkey(snakenew.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)

    snakenew.move()

screen.exitonclick()