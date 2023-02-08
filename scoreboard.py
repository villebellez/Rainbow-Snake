from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.points = 0
        with open("data.txt") as self.data:
            self.high_score = int(self.data.read())

    def update_points(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.points} - High Score: {self.high_score}", align="center", font=("Courier", 15, "bold"))

    def reset(self):
        if self.points > self.high_score:
            with open("data.txt", mode="w") as self.data:
                self.high_score =  self.points
                self.data.write(f'{self.high_score}')
        self.points = 0
        self.update_points()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", align="center", font=("Courier", 25, "bold"))

    def create_border(self, position, heading, forward):
        border = Turtle()
        border.color("grey")
        border.ht()
        border.penup()
        border.pensize(width=2)
        border.goto(position)
        border.pendown()
        border.setheading(heading)
        border.forward(forward)

    def create_borders(self):
        # Right Border
        self.create_border((290, 275), 270, 570)
        # Left Border
        self.create_border((-310, 275), 270, 570)
        # Up Border
        self.create_border((-310, 275), 0, 600)
        # Down Border
        self.create_border((-310, -295), 0, 600)