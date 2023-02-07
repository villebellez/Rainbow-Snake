import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=620, height=620)
screen.bgcolor("black")
screen.title("Rainbow Snake")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_on = True


def game_over():
    screen.update()
    time.sleep(3.5)
    snake.reset()


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()

    if snake.head.xcor() > 270 or snake.head.xcor() < -280 or snake.head.ycor() > 250 or snake.head.ycor() < -270:
        game_over()

    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            game_over()

screen.exitonclick()
