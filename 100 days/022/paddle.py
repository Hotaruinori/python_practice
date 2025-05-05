from turtle import Turtle
# Paddle, 用烏龜做
class Paddle(Turtle):
    MOVE_UP = (0, 20)
    MOVE_DOWN = (0, -20)
    def __init__(self,position):
        super().__init__()  #繼承烏龜
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()
        self.speed(0)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)