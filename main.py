from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game ')
screen.tracer(0)

screen.listen()
snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(lambda: snake.change_direction("up"), "Up")
screen.onkey(lambda: snake.change_direction("down"), "Down")
screen.onkey(lambda: snake.change_direction("left"), "Left")
screen.onkey(lambda: snake.change_direction("right"), "Right")

screen.update()
is_game_on = True


def validate_snake_out_of_bounds():
    ycor = snake.head.ycor()
    xcor = snake.head.xcor()
    return xcor > 290 or xcor < -290 or ycor > 290 or ycor < -290


def validate_head_hit_tail():
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            return True
    return False


def game_over():
    global is_game_on
    is_game_on = False
    score.announce_game_over()


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh_loc()
        snake.add_segment()
        score.increase_score()
    if validate_snake_out_of_bounds():
        game_over()
    if validate_head_hit_tail():
        game_over()

screen.exitonclick()
