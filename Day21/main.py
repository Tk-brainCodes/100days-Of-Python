import time
from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("coral")
screen.title("snake game")
screen.tracer(0)
screen.listen()

snake = Snake()
food_class = Food()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_playing = True

while is_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food_class) < 15:
        food_class.refresh()
        snake.extend()
        Scoreboard().increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_playing = False
        Scoreboard().game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_playing = False
            Scoreboard().game_over()

screen.exitonclick()


