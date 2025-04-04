import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# user play
# user_input = int(input("Please choose 0 for rock, 1 for scissors, and 2 for paper"))
#
# if user_input == 0:
#     print(rock)
# elif user_input == 1:
#     print(scissors)
# elif user_input == 2:
#     print(paper)
# else:
#     print("your play is invalid")

# As per solution, we are making the above more runtime efficient

play = [rock, scissors, paper]
user_input = int(input("Please choose 0 for rock, 1 for scissors, and 2 for paper"))
print(play[user_input])

# Computer Play
random_num = random.randint(0, 2)

print("Computer choose:")
print(play[random_num])

# Game Rules
if user_input >= 3 and random_num < 0: # to catch the invalid input
    print("You have input invalid number, You lose")
elif user_input == random_num:
    print('It is a draw')
elif user_input == 0 and random_num == 1:
    print("You win")
elif user_input == 1 and random_num == 2:
    print("You win")
elif user_input == 2 and random_num == 0:
    print("You win")
else:
    print("You lose")
