from move_snake import snake_move
from turtle import Screen

screen1 = Screen()
screen1.bgcolor("black")
screen1.title('My snake game')



p = snake_move()
p.head()
p.add_segment()

p.moving()



screen1.exitonclick()