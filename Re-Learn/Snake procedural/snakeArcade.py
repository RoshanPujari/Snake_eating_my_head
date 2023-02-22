import random
from turtle import Screen, Turtle
import time

#TODO setup the display for your snake game
wn = Screen()
wn.bgcolor("blue")
wn.setup(600, 600)

segment = []

wn.tracer(0)
#TODO make the snake head

snake_head = Turtle("square")
snake_head.color("black")
snake_head.penup()
snake_head.goto(0, 0)


#TODO make a food for the snake

food = Turtle("circle")
food.color("red")
food.shapesize(1)
food.penup()
food.goto(0, 100)

def move_up():
    if snake_head.heading() != 270:
        snake_head.setheading(90)

def move_down():
    if snake_head.heading() != 90:
        snake_head.setheading(270)

def move_right():
    if snake_head.heading() != 180:
        snake_head.setheading(0)

def move_left():
    if snake_head.heading() != 0:
        snake_head.setheading(180)

def move():
    pass

# wn.delay()

segment.append(snake_head)
game_over = False
while not game_over:
    #TODO Update the screen here

    wn.update()

    wn.listen()
    wn.onkey(move_up, key='Up')
    wn.onkey(move_down, key='Down')
    wn.onkey(move_right, key='Right')
    wn.onkey(move_left, key='Left')


    #Collision with food
    if snake_head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_block = Turtle("square")
        new_block.color("grey")
        new_block.penup()
        segment += [new_block]


    # wn.update()

    for index in range(len(segment)-1, 0, -1):

        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x, y)

    snake_head.forward(20)

    time.sleep(0.1)


    if snake_head.xcor() > 270 or snake_head.xcor() < -280 or snake_head.ycor() > 280 or snake_head.ycor() < -280:
        game_over = True
        write_turtle = Turtle()
        write_turtle.write("Game Over", align= "center", font=('Arial', 17, "normal"))
    print(segment)

    for block in [0, len(segment)-1]:
        if segment[block] != segment[0]:
            if segment[block].distance(segment[0]) < 10:
                game_over = True
                write_turtle = Turtle()
                write_turtle.write("Game Over", align="center", font=('Arial', 17, "normal"))

wn.exitonclick()