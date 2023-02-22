from turtle import Turtle, Screen
import random

class snakeMod():
    def __init__(self):
        self.score = 0
        self.segment = []


    def food(self):
        n_food = Turtle("circle")
        n_food.color("red")
        n_food.penup()
        n_food.shapesize(0.5)
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        n_food.setposition(x, y)

    def score_board(self):
        board = Turtle()
        board.pencolor("white")
        board.penup()
        board.hideturtle()
        board.setposition(x=0, y=250)
        board.write(f"Score: {self.score}", align="center", font=("Arial", 23, 'normal'))
