def init_screen(screen):
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('My Snake Game ')
    screen.tracer(0)


def init_listeners(screen, snake):
    screen.listen()
    screen.onkey(lambda: snake.change_direction("up"), "Up")
    screen.onkey(lambda: snake.change_direction("down"), "Down")
    screen.onkey(lambda: snake.change_direction("left"), "Left")
    screen.onkey(lambda: snake.change_direction("right"), "Right")
