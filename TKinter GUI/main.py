import tkinter
from tkinter import *


def button_clicked():
    print("I got clicked")
    my_text = input.get()
    my_label.config(text=my_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button

button1 = Button(text="Ok")
button1.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=3, row=3)

window.mainloop()
