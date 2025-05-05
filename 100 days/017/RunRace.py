from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_row = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for i in range(0, 6):
    T = Turtle(shape = "turtle")
    T.penup()
    T.color(colors[i])
    T.goto(x =-230, y = y_row[i])
    all_turtles.append(T)

if user_bet:
    is_race_on = True

while is_race_on:
    for T in all_turtles:
        if T.xcor()>230:
            is_race_on = False
            if user_bet == T.pencolor():
                print(f"You Win!! The winner is {T.pencolor()}")
            else:
                print(f"You Lose!! The winner is {T.pencolor()}")


        rand_distance = random.randint(0, 10)
        T.forward(rand_distance)






screen.exitonclick()
