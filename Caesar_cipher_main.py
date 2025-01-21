# TODO-1: Import and print the logo from art.py when the program starts.
from Casesar_cipher_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):

    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount  # option the index of current alphabet + the shift
            shifted_position %= len(alphabet)  # to the position beyond alpha length, eg: shift "z" by one >> shit to a
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

again_or_no = True

while again_or_no:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)  # call the above function again

    yes_or_no = input("Type 'yes; if you want to go again. otherwise, type 'no'\n").lower()

    if yes_or_no == 'no':
        again_or_no = False
        print("Goodbye")
