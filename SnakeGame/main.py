import time
from turtle import Screen
from snake import Snake
# Screen generation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# Character choice

snake = Snake()
snake.initialize_snake()

screen.listen()
screen.onkey(lambda: snake.move_in_directions(90), "Up")
screen.onkey(lambda: snake.move_in_directions(270), "Down")
screen.onkey(lambda: snake.move_in_directions(180), "Left")
screen.onkey(lambda: snake.move_in_directions(0), "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick()