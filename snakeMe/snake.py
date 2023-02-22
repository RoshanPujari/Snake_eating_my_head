from turtle import Turtle

class Snake:
    def __init__(self):

        starting_position = [(0, 0), (-20, 0), (-40, 0)]
        segment = []

        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setposition(position)
            segment.append(new_segment)

    def move(self, segment):
        for seg in range(len(segment) - 1, 0, -1):
            new_x = segment[seg - 1].xcor()
            new_y = segment[seg - 1].ycor()

            segment[seg].goto(new_x, new_y)

        segment[0].forward(20)