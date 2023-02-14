from turtle import Turtle, colormode

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_snake = 20
up = 90
down = 270
left = 180
right = 0
colormode(255)


class Snake:
    def __init__(self):
        self.colors_num = 0
        self.colors_list = [[250, 145, 137], [252, 174, 124], [255, 230, 153], [249, 255, 181], [179, 245, 188],
                            [214, 246, 255], [226, 203, 247], [209, 189, 255]]
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def color(self):
        if self.colors_num >= 8:
            self.colors_num = 0
        self.colors = self.colors_list[self.colors_num]
        self.colors_num += 1
        r = self.colors[0]
        g = self.colors[1]
        b = self.colors[2]
        self.snake_part.color(r, g, b)
        return self.colors_num

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
        self.colors_num = 0
        self.create_snake()
        self.head = self.snake_parts[0]
        return self.colors_num
