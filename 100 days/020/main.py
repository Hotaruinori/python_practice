from turtle import Screen
import time # 導入用sleep來讓 update影響畫慢更新的速度
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(height= 600, width= 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0) #當預設的 tracer 被關閉時，就可以用update來更新畫面

snack = Snake()# 調用snake.py的功能
food = Food()# 調用food.py的功能
score_board = ScoreBoard()

screen.listen()
screen.onkey(snack.up,"Up")
screen.onkey(snack.down,"Down")
screen.onkey(snack.left,"Left")
screen.onkey(snack.right,"Right")

game_is_on = True
while game_is_on:
    screen.update() #更新畫面，放在for迴圈外可以讓每個turtle動完再一次更新
    time.sleep(0.1) #for迴圈外可以讓每個turtle動完才暫停一下，讓蛇動快點
    snack.move()
    #檢測與food的碰撞
    if snack.head.distance(food) < 15:
        food.refresh()
        snack.extend()
        score_board.increase_score()
    #檢測與牆壁碰撞
    if snack.head.xcor() > 295 or snack.head.xcor() < -295 or snack.head.ycor() > 295 or snack.head.ycor() < -295:
        # game_is_on = False
        # score_board.game_over()
        score_board.reset()
        snack.reset()
    #檢測與身體的碰撞
    for segment in snack.segments[1:]:
        if snack.head.distance(segment) < 5:
            # game_is_on = False
            # score_board.game_over()
            score_board.reset()
            snack.reset()



screen.exitonclick()