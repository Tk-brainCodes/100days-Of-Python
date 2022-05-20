import time
from turtle import Turtle, Screen
import random


screen = Screen()
turtle = Turtle()

screen.setup(width=600, height=600)
screen.tracer(0)

'# car manager constant'
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_DISTANCE = 5
MOVE_INCREMENT = 10

'# player constant'
STARTING_POSITION = (0, -280)
STARTING_MOVE_POSITION = 5
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

'# scoreboard constant'
FONT = ("Courier", 24, "normal")

'# player function'
player_turtle = Turtle()
player_turtle.shape("turtle")
player_turtle.penup()
player_turtle.goto(STARTING_POSITION)
player_turtle.setheading(90)


def move_up():
    player_turtle.forward(MOVE_DISTANCE)


def is_at_finish_line():
    if player_turtle.ycor() > FINISH_LINE_Y:
        return True
    else:
        return False


def goto_starting_position():
    player_turtle.goto(STARTING_POSITION)


screen.listen()
screen.onkey(move_up, "Up")

'# car manager function'
all_cars = []
car_speed = STARTING_MOVE_POSITION


def create_new_car():
    random_chance = random.randint(1, 6)
    if random_chance == 1:
        car_turtle = Turtle()
        car_turtle.shape("square")
        car_turtle.shapesize(stretch_wid=1, stretch_len=2)
        car_turtle.penup()
        car_turtle.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        car_turtle.goto(300, random_y)
        all_cars.append(car_turtle)


def move_cars():
    for cars in all_cars:
        cars.backward(car_speed)


def level_up():
    global car_speed
    car_speed += MOVE_INCREMENT


'# scoreboard function'
level = 1
score_board = Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(-280, 250)
score_board.write(f"Level {level}", align="left", font=FONT)


def increase_level():
    global level
    level += 1
    score_board.clear()
    score_board.write(f"Level {level}", align="left", font=FONT)


def game_over():
    score_board.goto(0, 0)
    score_board.write("GAME OVER!", align="center", font=FONT)


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    create_new_car()
    move_cars()

    '# Detect collision'
    for car in all_cars:
        if car.distance(player_turtle) < 20:
            game_is_on = False
            game_over()

    '# Detect successful crossing'
    if is_at_finish_line():
        goto_starting_position()
        level_up()
        increase_level()


screen.exitonclick()