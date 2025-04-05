from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

# -----------------------DATA READ IN-----------------------------
try:
    data = pd.read_csv('data/word_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('./data/french_words.csv')
# to show each column value as a list
data_list = data.to_dict(orient="records")  # to covert df to dict in this format [{a:b,c:d},{a:e,c:f}]
current_card = {}


# -----------------------CHECK AND SAVED-------------------------------
def known_word():
    data_list.remove(current_card)
    df = pd.DataFrame(data_list)
    df.to_csv('data/word_to_learn.csv', index=False)
    next_card()


# -----------------------NEXT CARD-------------------------------
def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)  # everytime the card flip, reset the timer
    current_card = choice(data_list)
    canvas.itemconfig(text_title, text="French", fill='black')
    canvas.itemconfig(text_word, text=current_card['French'], fill='black')
    canvas.itemconfig(front_canvas, image=image_front)
    flip_timer = window.after(3000, flip)  # set the new timer


# -----------------------FLIP MECHANISM-------------------------------
def flip():
    canvas.itemconfig(front_canvas, image=image_back)
    canvas.itemconfig(text_title, text="English", fill='white')
    canvas.itemconfig(text_word, text=current_card["English"], fill='white')


# -----------------------USER INTERFACE-----------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip)  # the first time timer start
# Canvas
image_front = PhotoImage(file="./images/card_front.png")
image_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_canvas = canvas.create_image(400, 263, image=image_front)
text_title = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
text_word = canvas.create_text(400, 263, text="word", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Button
image_x = PhotoImage(file="./images/wrong.png")
button_x = Button(image=image_x, highlightthickness=0, command=next_card)
button_x.grid(row=1, column=0)
image_tick = PhotoImage(file="./images/right.png")
button_tick = Button(image=image_tick, highlightthickness=0, command=known_word)
button_tick.grid(row=1, column=1)

next_card()  # to start off with next card

window.mainloop()

