from art import logo
import random


def game():

    print(logo)
    print("""
        Welcome to the Number Guessing Game !
        I'm thinking of a number between 1 and 100.
        """)
    difficulty = input("Choose difficulty. Type 'easy' or 'hard: ").lower()

    if difficulty == 'easy':
        attempt = 10
        print(f"You have {attempt} attempts remaining to guess the number.")
    elif difficulty == 'hard':
        attempt = 5
        print(f"You have {attempt} attempts remaining to guess the number.")
    else:
        print('Invalid difficulty level')
        attempt = 0

    random_number = random.randrange(1, 100)
    guess = int(input("make a guess:"))

    while True:
        if attempt == 1:
            print(f"You are running out of attempt. Game Over")
            break
        else:
            if guess == random_number:
                print(f"You got it! The answer was {guess}.")
                break
            elif guess > random_number:
                attempt -= 1
                print(f"Too high.\n"
                      f"You have {attempt} remaining to guess the number.")
                guess = int(input("Guess again."))
            elif guess < random_number:
                attempt -= 1
                print(f"Too low.\n"
                      f"You have {attempt} remaining to guess the number.")
                guess = int(input("Guess again."))


while input("Do you want to play again?Y/N").lower () == "y":
    print("\n"*20)
    game()

