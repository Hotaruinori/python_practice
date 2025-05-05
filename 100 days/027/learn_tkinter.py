import tkinter

def button_clicked():
    print("I got clicked")
    next_text = input_text.get()
    my_label.config(text=next_text)

#建立新視窗與配置
window = tkinter.Tk()
window.title("Widget Examples")
window.minsize(width=500, height= 300)
window.config(padx=100,pady=200)

window.config(padx=100,pady=200)

#Butten
button = tkinter.Button(text="Click me", command= button_clicked)
# button.pack()
button.grid(column=1, row=1)

#Butten2
button2 = tkinter.Button(text="Click me", command= button_clicked)
# button.pack()
button2.grid(column=2, row=0)

#Entry
input_text = tkinter.Entry(width=10)
# input_text.pack()
input_text.grid(column=3, row=2)





window.mainloop()
