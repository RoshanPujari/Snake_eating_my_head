from turtle import Turtle

class snake_move():
    def __init__(self):
        self.segment = []

    def head(self):
        head_snake = Turtle('square')
        head_snake.color('grey')
        head_snake.setposition(0, 0)
        self.segment.append(head_snake.position())

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        self.segment.append(new_segment.position())


    def move_up(self):
        self.segment