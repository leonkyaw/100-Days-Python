#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as file:
    name_list = file.readlines()

# read the invitation letter
with open("./Input/Letters/Starting_letter.txt") as temp:
    contents = temp.read()

# create the invitation and saved in the output folder
for name in name_list:
    new_name = name.strip("\n")
    with open(f"./Output/ReadyToSend/{new_name}.docx", mode='w') as invite:
        invite.write(contents.replace("[name]", new_name))
