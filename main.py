import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=620, height=620)
screen.bgcolor("black")
screen.title("Rainbow Snake")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
