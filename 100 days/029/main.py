from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint

import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers= [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    input_text3.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_text1.get()
    email = input_text2.get()
    password = input_text3.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="請不要留空白")
    else:
        try:
            with open("data.json", "r") as data_file:
                #read old date
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            input_text1.delete(0, END)
            input_text3.delete(0, END)
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def find_password():
    website = input_text1.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="還沒有儲存過任何網站的密碼")
    else:
        if input_text1.get() in data:
            pwd = data.get(website).get("password")
            email = data[website]["email"]
            messagebox.showinfo(title=website, message=f"Email:{email},\n Password：{pwd}, \n已複製密碼，可直接到網站貼上~")
            pyperclip.copy(pwd)
            input_text3.insert(0, pwd)
        else:
            messagebox.showinfo(title="Oops!", message=f"還沒有儲存過{website}這個網站的密碼")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#鎖頭本體
canvas = Canvas(width=200 , height= 200 , highlightthickness=0, )
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image )
canvas.grid(column=1 , row=0 )

#左側文字
label1 = Label(text="Website:")
label1.grid(column=0 , row=1 )
label2 = Label(text="Email/Username:")
label2.grid(column=0 , row=2 )
label3 = Label(text="Password:")
label3.grid(column=0 , row=3 )

#輸入框
input_text1 = Entry(width=18)
input_text1.grid(column=1, row=1)
input_text1.focus()
input_text2 = Entry(width=35)
input_text2.grid(column=1, row=2 , columnspan= 2)
input_text2.insert(0, "hotaruinori@hotmail.com")
input_text3 = Entry(width=18)
input_text3.grid(column=1, row=3 )

#按鈕
button1 = Button(text="Generate Password", command=generate_password)
button1.grid(column=2 , row=3 )
button2 = Button(text="Add", width=36, command=save)
button2.grid(column=1, row=4 , columnspan= 2)
button3 = Button(text="Search",width=16, command=find_password)
button3.grid(column=2, row=1 , columnspan= 2)



window.mainloop()