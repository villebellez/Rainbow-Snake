from random import randint
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = randint(-275, 265)
        random_y = randint(-265, 245)
        self.goto(random_x, random_y)
