from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # quiz_brain as data type QuizBrain
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,  # wrap text
            text="Amazon acquired Twitch in\nAugust 2014 for $970 million\ndollars",
            font=('Arial', 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.label.grid(row=0, column=1)
        check_image = PhotoImage(file='images/true.png')
        unknown_image = PhotoImage(file='images/false.png')
        self.button_check = Button(image=check_image, highlightthickness=0, command=self.yes)
        self.button_check.grid(row=2, column=0)
        self.button_unknown = Button(image=unknown_image, highlightthickness=0, command=self.no)
        self.button_unknown.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(background='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_check.config(state='disabled')
            self.button_unknown.config(state='disabled')

    def yes(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def no(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

