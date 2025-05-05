import turtle

import pandas
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"  #turtle只接受gif檔
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
#點擊畫面可以印出座標
# def get_mouse_click_door(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_door)
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct",
                                    prompt= "What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States to learn.csv")
        break
    #檢查輸入值是否在50州之內
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item()) # 如果沒有用.item()方法去提state_data.x，會連編號一起產出
        t.write(state_data.state.item())





# screen.exitonclick()
# screen.mainloop()