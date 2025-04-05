import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_letter = ""
pass_symbols = ""
pass_numbers = ""

for n_letter in range(1, nr_letters+1): # we can logically change range(0, nr_letter)
    pass_letter += letters[random.randint(1, len(letters)-1)]
    # pass_letter += random.choice(letters)
print(pass_letter)

for n_symbols in range(1, nr_symbols+1):
    pass_symbols += symbols[random.randint(1, len(symbols)-1)]
    # pass_symbols += random.choice(symbols)
print(pass_symbols)

for n_numbers in range(1, nr_numbers+1):
    pass_numbers += numbers[random.randint(1, len(numbers)-1)]
    # pass_numbers += random.choice(numbers)
print(pass_numbers)

# password randomized (1st method)
password = pass_letter + pass_symbols + pass_numbers
# final_password = random.sample(password, len(password)) # this will return as list
# print(''.join(final_password)) # to convert list to string

# reshuffle function randomized (2nd method)
pass_ls = list(password)
random.shuffle(pass_ls) # this won't create the new list, only shuffle the order

print(pass_ls)

# change it back to string
final_password = ""

for char in pass_ls:
    final_password += char
print(final_password)
