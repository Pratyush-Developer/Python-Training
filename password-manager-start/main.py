import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for char in range(randint(8, 10))]
    symbol_list = [choice(symbols) for char in range(randint(2, 4))]
    number_list = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_clicked():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving new data
                json.dump(new_data, file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search Website ------------------------ #

def search():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data_dict = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data_dict:
            email = data_dict.get(website).get('email')
            password = data_dict.get(website).get('password')
            messagebox.showinfo(title=f"{website}", message=f"Email: {email} "
                                                            f"\nPassword: {password}")
        else:
            messagebox.showerror(title=f"{website}", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Label Website
label_website = Label(text="Website:", font=("Ariel", 14))
label_website.grid(column=0, row=1)

# Label Email
label_email = Label(text="Email/Username:", font=("Ariel", 14))
label_email.grid(column=0, row=2)

# Label Password
label_password = Label(text="Password:", font=("Ariel", 14))
label_password.grid(column=0, row=3)

# Website Entry
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()

# Search Button
search_button = Button(text="Search", width=10, command=search)
search_button.grid(column=2, row=1)

# Username Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "arish@gmail.com")

# Password Entry
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

# Generate Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, command=add_button_clicked)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
