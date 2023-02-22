from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey")
# TODO 1: Create a snake body.
starting_position = [(0, 0), (-20, 0), (-40, 0)]
screen.tracer(0)
segment = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setposition(position)
    segment.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg in range(len(segment)-1, 0, -1):
        new_x = segment[seg-1].xcor()
        new_y = segment[seg-1].ycor()

        segment[seg].goto(new_x, new_y)

    segment[0].forward(20)

screen.exitonclick()