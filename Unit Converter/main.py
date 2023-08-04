import tkinter
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def button_clicked():
    distance = int(user_input.get()) * 1.6
    result_label.config(text=distance)


# Label 1
miles_label = tkinter.Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=2, row=0)

# Label 2
equal_label = tkinter.Label(text="is equal to", font=("Arial", 16, "bold"))
equal_label.grid(column=0, row=1)

# Label 3
km_label = tkinter.Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=1)

# Label 4
result_label = tkinter.Label(text="0", font=("Arial", 16, "bold"))
result_label.grid(column=1, row=1)

# button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
user_input = Entry(width=8)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)

window.mainloop()
