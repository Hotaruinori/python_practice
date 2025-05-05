import tkinter

# 視窗起始
window = tkinter.Tk()
window.title("Mile to Km Converter ")
window.minsize(width=300 , height= 150)
window.config(padx= 20, pady= 20)

def calculate():
    label4.config(text= round(int(text.get())/0.6213))

# 輸入框
text = tkinter.Entry(width=10)
text.insert(index=0 ,string="0")
text.grid(column=1 , row=0 )

#label
label1 = tkinter.Label(text="is equal to")
label1.grid(column=0, row=1)

label2 = tkinter.Label(text="Miles")
label2.grid(column=2, row=0)

label3 = tkinter.Label(text="Km")
label3.grid(column=2, row=1)

label4 = tkinter.Label(text="0")
label4.grid(column=1, row=1)

#button
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)




window.mainloop()