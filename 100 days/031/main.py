from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    origin_data = pandas.read_csv("data/english_words.csv")
    to_learn = origin_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    #這邊canvas的語法不一樣
    canvas.itemconfig(card_title, text = "English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = screen.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Chinese", fill="white")
    canvas.itemconfig(card_word, text=current_card["Chinese"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data2 = pandas.DataFrame(to_learn)
    print(len(to_learn))
    data2.to_csv("data/words_to_learn.csv", index=False)
    next_card()

screen = Tk()
screen.title("Flashy Word Cards")
screen.config(padx= 50, pady=50 ,bg=BACKGROUND_COLOR)
#翻牌
flip_timer = screen.after(3000, func=flip_card)


#畫布
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic") )
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold") )
canvas.grid(column=0 ,row=0, columnspan=2)

#按鈕
yes_image = PhotoImage(file="images/right.png")
button1 = Button(image=yes_image, highlightthickness=0, command=is_known)
# button1.config(width=60, height=60)
button1.grid(column= 1, row= 1)

no_image = PhotoImage(file="images/wrong.png")
button2 = Button(image=no_image, highlightthickness=0, command=next_card)
# button2.config(width=60, height=60)
button2.grid(column= 0, row= 1)



next_card()







screen.mainloop()
