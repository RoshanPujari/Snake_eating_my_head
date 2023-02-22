from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey")
screen.tracer(0)
# TODO 1: Create a snake body.
starting_position = [(0, 0), (-20, 0), (-40, 0)]

snakenew = Snake()
food = Food()
current_score = Score()
#listen to the key pressed
screen.listen()


# Keys to control the snake
screen.onkey(snakenew.up, "Up")
screen.onkey(snakenew.down, "Down")
screen.onkey(snakenew.left, "Left")
screen.onkey(snakenew.right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()
    snakenew.move()

    # Detect collision with food

    if snakenew.head.distance(food) < 15:
        food.refresh()
        snakenew.extend()
        print(current_score.increase_score())

    # Detect collision with wall

    if snakenew.head.xcor() > 280 or snakenew.head.xcor() < -300 or snakenew.head.ycor() > 300 or snakenew.head.ycor() < -280:
        game_is_on = False
        current_score.game_over()

    # Detect collision with tail
    # if the head collides with any segment of the tail:
        # trigger game_over

    for segment in snakenew.segment:
        if segment == snakenew.head:
            pass
        elif snakenew.head.distance(segment) < 10:
            game_is_on = False
            current_score.game_over()

screen.exitonclick()