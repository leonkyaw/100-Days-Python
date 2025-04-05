import turtle
import pandas as pd
import check as c

welcome_title = "Guess The State"
welcome_prompt = "What's another state name?"
total_state = 50
state_guessed = []
screen = turtle.Screen()
screen.title('U.S. State Game')
# adding image to the turtle
image = "blank_states_img.gif"  # make sure the name matched
screen.addshape(image)
turtle.shape(image)

check = c.Check()


while len(state_guessed) < 50:
    answer_state = screen.textinput(title=welcome_title, prompt=welcome_prompt).title()

    if answer_state == "Exit":
        new_list = [state for state in c.state_list if state not in state_guessed]
        # new_list =[]
        # for state in c.state_list:
        #   if state not in state_guessed:
        #       new_list.append(state)
        dict = {"state": new_list}
        df = pd.DataFrame(dict)
        df.to_csv('learn.csv')
        break
    if check.check_answer(answer_state):
        state_guessed.append(answer_state)
        welcome_title = f"{len(state_guessed)}/{total_state} Guess The State"
