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
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(TIMER)  # this is to stop the timer so that we can make change to other variable
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS <= 8:  # to stop the timer if beyond 8 reps, can remove it to let the timer run.
        if REPS % 8 == 0:
            count_down(long_break_sec)
            title_label.config(text="Break", fg=RED)
        elif REPS % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text="Break", fg=PINK)
        else:
            count_down(work_sec)  # this function can only be called after we have created the canvas
            title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)  # this function return largest whole number
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # this is the dynamic typing,changing the data type of variable by changing content

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)  # assign to variable so that, the timer can be stopped
    else:
        start_timer()  # when the timer hit zero, we call the start_timer again
        if REPS % 2 == 0:  # every two reps completed, added the check mark
            marks = int(REPS / 2)
            check_mark.config(text="✔"*marks)
        # Alternative to above
        # work_session = math.floor(REPS/2)
        # for _ in range(work_session)
        #   marks += "✔"
        # check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # change background and remove canvas border
tomato_img = PhotoImage(file="tomato.png")  # read in the image
canvas.create_image(100, 112, image=tomato_img)  # create the image on canvas
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))  # create text
canvas.grid(row=2, column=2)  # display what we have created


# to create label "Timer" and "tick" out of canvas
title_label = Label(text="Timer", font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW)
title_label.grid(row=1, column=2)
check_mark = Label(font=(FONT_NAME, 18), fg=GREEN, bg=YELLOW)
check_mark.grid(row=4, column=2)

# create start and reset buttons
start = Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
start.grid(row=3, column=1)
reset = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightthickness=0)
reset.grid(row=3, column=3)

window.mainloop()
