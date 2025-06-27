from tkinter import *
from tkinter import messagebox
from word_dict import data
import random

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CORRECT = 0
WORD_COUNT = 0
STARTING_TIME = 60
NUM_CHAR = 0
TIMER = None
words_show = random.sample(data, 21)


#------- check for correct word ---------
def check(event):
    word_input = word_entry.get().strip(' ')
    global NUM_CHAR
    NUM_CHAR += len(word_input)

    global CORRECT, WORD_COUNT, words_show
    WORD_COUNT += 1
    word_entry.delete(0, END)

    if WORD_COUNT % 14 == 0:
        words_show = words_show[14:]
        words_show = words_show + random.sample(data, 14)
        canvas.itemconfig(display_words, text=words_show)
    else:
        words_show = words_show
        canvas.itemconfig(display_words, text=words_show)

    if word_input in words_show:
        CORRECT += 1

    corrected_percent = round(CORRECT/WORD_COUNT * 100, 2)
    corrected_value.config(text=f'{corrected_percent}%')


#------- COUNTDOWN ------------
def timer(count):
    time_value.config(text=f"{count}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, timer, count - 1)
    else:
        messagebox.showinfo("Score Summary", f"You Accuracy is {round(CORRECT/WORD_COUNT * 100, 2)}%, "
                                             f"Your WPM is {NUM_CHAR/5}")
        window.destroy()


#------- UI Setup ----------
window = Tk()
window.title('Typing Speed Test')
window.config(padx=100, pady=50, bg=GREEN)


canvas = Canvas(width=500, height=300, bg=YELLOW, highlightthickness=1)
display_words = canvas.create_text(250, 150, text=words_show, width=500, font=("Arial", 35, "normal"), fill='black',
                                   justify="center", anchor="center")
canvas.grid(row=2, column=1, columnspan=6)

word_entry = Entry(width=55, fg='black')
word_entry.config(bg=YELLOW, highlightthickness=0, insertbackground='black')
word_entry.focus()
word_entry.grid(row=4, column=1, columnspan=6)

# to create label
corrected_word_label = Label(text="Corrected Word:", font=("Arial", 15, 'normal '), fg=YELLOW, bg=GREEN)
corrected_word_label.grid(row=1, column=1)
corrected_value = Label(text="00.00%", font=("Arial", 15, 'normal '), fg=GREEN, bg=YELLOW, highlightthickness=1)
corrected_value.grid(row=1, column=2)
WPM_label = Label(text="WPM:", font=("Arial", 15, 'normal '), fg=YELLOW, bg=GREEN)
WPM_label.grid(row=1, column=3)
WPM_value = Label(text="120", font=("Arial", 15, 'normal '), fg=GREEN, bg=YELLOW, highlightthickness=1)
WPM_value.grid(row=1, column=4)
time_label = Label(text="Time Left:", font=("Arial", 15, 'normal '), fg=YELLOW, bg=GREEN)
time_label.grid(row=1, column=5)
time_value = Label(text="60", font=("Arial", 15, 'normal '), fg=GREEN, bg=YELLOW, highlightthickness=1)
time_value.grid(row=1, column=6)

timer(STARTING_TIME)
window.bind_all("<space>", check)
window.mainloop()
