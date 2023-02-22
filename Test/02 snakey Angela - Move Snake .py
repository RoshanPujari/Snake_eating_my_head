from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey")
# screen.tracer(0)
# TODO 1: Create a snake body.
starting_position = [(0, 0), (-20, 0), (-40, 0)]

snakenew = Snake()

game_is_on = True
while game_is_on:
    # screen.update()
    # time.sleep(0.1)

    snakenew.move()

screen.exitonclick()