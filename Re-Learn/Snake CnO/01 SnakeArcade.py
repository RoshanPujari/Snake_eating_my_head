from turtle import Screen, Turtle
import time
import random
from snakeclass import snakeMod
from move_snake import snake_move

#display area for the snake game

screen1 = Screen()
screen1.bgcolor("black")
screen1.title("Snake Arcade")
screen1.setup(600, 600)

screen1.delay(20)


sb = snakeMod()
sb.score_board()

#main stating head of the snake

sb.food()


screen1.listen()
















screen1.exitonclick()