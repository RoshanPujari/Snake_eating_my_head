from turtle import Screen, Turtle
import time

def turn_up():
    segment[0].speed(90)
    segment[0].setheading(90)


def turn_down():
    segment[0].speed(90)
    segment[0].setheading(270)

def turn_left():
    segment[0].speed(90)
    segment[0].setheading(180)


def turn_right():
    segment[0].speed(90)
    segment[0].setheading(0)


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

    for seg_num in range(len(segment)-1, 0,  -1):
        new_x = segment[seg_num-1].xcor()
        new_y = segment[seg_num-1].ycor()

        segment[seg_num].goto(new_x, new_y)
    segment[0].forward(20)

    screen.onkeypress(key="Down", fun=turn_down)
    screen.onkeypress(key="Up", fun= turn_up)
    screen.onkeypress(key="Right", fun=turn_right)
    screen.onkeypress(key="Left", fun=turn_left)

    screen.listen()

screen.exitonclick()

