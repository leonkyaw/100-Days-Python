from morse import Morse_Code


def check_dict(letter):
    '''
        This function will check if the letter is in the morse dictionary, if not it will return the letter itself.
        If the letter exist, return the related word.
    '''
    if letter not in Morse_Code.values():
        return letter

    for key, value in Morse_Code.items():
        if value == letter:
            return key


def encoder(message):
    """
    This will encode the message, special character such as '?' won't be transformed and it will be stored as it is.
    """
    word_list = message.upper().split()
    encode_message = ''
    for n in range(len(word_list)):
        for letter in word_list[n]:
            try:
                encode_message += f'{Morse_Code[letter]} '
            except KeyError:
                encode_message += letter
        if n != len(word_list)-1:
            encode_message += '/ '
    print(encode_message)


def decoder(message):
    """
    Decoding message, it will call upon the check_dict function and return the corresponding alphabet to the code
    """
    word_list = message.split('/ ')
    letter_list = []
    decode_message = ''
    for word in word_list:
        letter_list.append(word.split())

    for n in range(len(letter_list)):
        for letter in letter_list[n]:
            decode_message += check_dict(letter)
        if n != len(letter_list)-1:
            decode_message += ' '

    print(decode_message.capitalize())


encoder('I am so HUNGRY!!!')
decoder('·· / ·– –– / ··· ––– / ···· ··– –· ––· ·–· –·–– !!!')
