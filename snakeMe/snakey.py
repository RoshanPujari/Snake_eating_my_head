from turtle import Screen, Turtle

tikle = Turtle()
screen = Screen()

def turn_up():
    tikle.speed(90)
    tikle.setheading(90)


def turn_down():
    tikle.speed(90)
    tikle.setheading(270)

def turn_left():
    tikle.speed(90)
    tikle.setheading(180)


def turn_right():
    tikle.speed(90)
    tikle.setheading(0)

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# TODO 1: Create a snake body.
while True:
    screen.delay(50)
    tikle.color("white")
    tikle.shape("turtle")
    tikle.penup()

    tikle.forward(10)

    screen.onkeypress(key="Down", fun=turn_down)
    screen.onkeypress(key="Up", fun= turn_up)
    screen.onkeypress(key="Right", fun=turn_right)
    screen.onkeypress(key="Left", fun=turn_left)

    screen.listen()
screen.exitonclick()