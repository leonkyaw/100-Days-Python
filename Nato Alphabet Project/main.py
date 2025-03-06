import pandas as pd

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

data = pd.read_csv('nato_phonetic_alphabet.csv')
# data.to_dict() >> it is not return the format we wanted to, need to use dictionary comprehension
nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please input your word: ").upper()
result = [nato_dictionary[letter] for letter in user_input]
print(result)
