from turtle import Screen, Turtle


screen = Screen()
tikle_all = []
# TODO 1: Create a snake body.
screen.delay(50)
num = 0
for i in range(3):

    tikle = Turtle()
    tikle.color("black")
    tikle.shape("square")
    tikle.penup()
    tikle.goto(0+num, 0)
    tikle_all.append(tikle)
    num += 20
for k in tikle_all:
    k.forward(100)

screen.exitonclick()
