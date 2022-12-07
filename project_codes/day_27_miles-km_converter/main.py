from tkinter import *


def calculate():
    """converts the input miles to km"""
    km = float(miles_entry.get()) * 1.6
    km_answer.config(text=round(km))


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=30, pady=30)

# create an entry
miles_entry = Entry(width=10)
miles_entry.grid(row=0, column=1)
miles_entry.focus()

# create a label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)
km_answer = Label(text=0)
km_answer.grid(row=1, column=1)
km_label = Label(text="Km")
km_label.grid(row=1, column=2)

# create a button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
