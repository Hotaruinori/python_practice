import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
s = Screen()
s.setup(width = 800, height = 600)
s.bgcolor("black")
s.title("Pin-Pong")
s.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")
s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    s.update()

    # 頂部底部碰撞 #反彈
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    # 右邊paddle反彈
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.rf_bounce()
    # 超過邊界
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.increase_r_score()
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.increase_l_score()

s.exitonclick()
