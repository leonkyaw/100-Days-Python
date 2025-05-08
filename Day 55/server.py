from flask import Flask
from random import randint

random_number = randint(0, 9)
print(random_number)
app = Flask(__name__)

@app.route('/')
def main_page():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>')


@app.route('/<int:guess>')
def number_check(guess):
    if guess > random_number:
        return ("<h1 style='color:red'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=200>")
    elif guess < random_number:
        return ("<h1 style='color:green'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=200>")
    else:
        return ("<h1 style='color:purple'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=200>")


if __name__ == '__main__':
    app.run(debug=True)
