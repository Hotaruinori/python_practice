from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def star_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        count_down(long_break_sec)
        time_label.config(text="Long Break" , fg=RED )
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        time_label.config(text="Short Break", fg=PINK)
    else :
        count_down(work_sec)
        time_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        star_timer()
        marks = ""
        work_sessions = math.floor(reps % 2 )
        for _ in range(work_sessions):
            marks += "✔️"
        check_marks.config(text = marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg=YELLOW)


#番茄本體
canvas = Canvas(width=200 , height= 224 , bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image )
timer_text = canvas.create_text(100, 130, text= "00:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1 , row=1 )



#上方文字
time_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
time_label.grid(column=1 , row=0 )


#按鈕
#Buttons
button1 = Button(text="Start", command=star_timer, highlightthickness=0)
button1.grid(column=0 , row=2 )
button2 = Button(text="Reset", command=reset_timer, highlightthickness=0)
button2.grid(column=2 , row=2)
#勾勾
check_marks = Label(text="", bg=YELLOW, fg=GREEN)
check_marks.grid(column=1 , row=3 )


window.mainloop()