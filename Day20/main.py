import time
from turtle import Screen
from snake_class import Snake
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
screen.listen()

snake = Snake()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_playing = True

while is_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()
















screen.exitonclick()


