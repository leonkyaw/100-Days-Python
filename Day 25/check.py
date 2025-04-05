import pandas as pd
from turtle import Turtle

FONT = ("Ariel", 10, "normal")
data = pd.read_csv("50_states.csv")
state_list = data['state'].to_list()
x_list = data['x'].to_list()
y_list = data['y'].to_list()


class Check(Turtle):

    def __int__(self):
        super().__init__()

    def write_message(self, answer, cor):
        self.penup()
        self.hideturtle()
        self.goto(cor)
        self.write(arg=f"{answer.title()}", align="center", font=FONT)

    def check_answer(self, answer):
        if answer in state_list:
            x_corr = x_list[state_list.index(answer.title())]
            y_corr = y_list[state_list.index(answer.title())]
            cor = (x_corr, y_corr)
            self.write_message(answer, cor)
            return True




