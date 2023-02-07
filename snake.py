from turtle import Turtle, colormode
from random import randrange

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_snake = 20
up = 90
down = 270
left = 180
right = 0
colormode(255)


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def color(self):
        R = randrange(50, 257, 10)
        G = randrange(50, 257, 10)
        B = randrange(50, 257, 10)
        self.snake_part.color(R, G, B)

    def add_segment(self, position):
        self.snake_part = Turtle("square")
        self.snake_part.penup()
        self.color()
        self.snake_part.goto(position)
        self.snake_parts.append(self.snake_part)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):  # Start Stop Step
            x = self.snake_parts[part - 1].xcor()
            y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(x, y)
        self.snake_parts[0].forward(move_snake)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def reset(self):
        for body in self.snake_parts:
            body.reset()
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]
