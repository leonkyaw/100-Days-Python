from tkinter import *  # this is import Class, not messagebox
from tkinter import messagebox  # to get the messagebox module
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8,10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

    # put the password in the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # validation check if there is any blank input
    if len(website) == 0:
        messagebox.showinfo(title="Something Wrong!", message="You shouldn't leave your website info empty!")
    elif len(password) == 0:
        messagebox.showwarning(title="Something Wrong!", message="You shouldn't leave your password info empty!")
    else:
        # message box to check if they are happy with the input.
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered\n"
                                               f"Email:{email}\nPassword:{password}\nIt is ok to save")
        if is_ok:
            with open("data.txt", 'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)  # start of the range, end of the range
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Set up window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo creation
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=1, column=2)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=2, column=1)
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)
password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()  # to start the cursor in this input box
email_entry = Entry(width=35)
email_entry.grid(row=3, column=2, columnspan=2)
email_entry.insert(0, "leon@gmail.com")  # index,string >>index = 0 = at the start,END = end of previous str
password_entry = Entry(width=21)
password_entry.grid(row=4, column=2)

# Buttons
gen_password = Button(width=10, text="Generate Password",command=generate_password)
gen_password.grid(row=4, column=3)
add_button = Button(width=33, text="Add", command=save)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
