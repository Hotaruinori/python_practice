from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        nex_y = self.ycor() + self.y_move
        self.goto(new_x, nex_y)

    def bounce(self):
        self.y_move *= -1

    def rf_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9 #讓球越打越快

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1