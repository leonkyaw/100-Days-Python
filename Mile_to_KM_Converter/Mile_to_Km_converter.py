from tkinter import *


def button_click():
    miles = float(entry.get())
    result = round(miles * 1.609, 2)
    label2.config(text=str(result))


# to create the window
window = Tk()
window.minsize(width=300, height=150)
window.title("Mile to Kilometer Converter")
window.config(padx=30, pady=30)

# to create the label
label = Label(text='Miles', font=('Ariel', 15))
label.grid(row=0, column=3)
label1 = Label(text='is equal to', font=('Ariel', 15))
label1.grid(row=1, column=0)
label2 = Label(text='0', anchor=CENTER, font=('Ariel', 15))
label2.grid(row=1, column=1)
label3 = Label(text='Km', font=('Ariel', 15))
label3.grid(row=1, column=3)

# to create entry
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

# to create button

button = Button(text="Calculate", command=button_click)
button.grid(row=2, column=1)

window.mainloop()