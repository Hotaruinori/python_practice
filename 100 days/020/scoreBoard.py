from turtle import Turtle
ALIGNMENT ="center"
FONT=("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode= "r") as data:
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
        self.penup()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score ： {self.score} High Score ： {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()