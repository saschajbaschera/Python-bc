from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=12, use_digits=True, use_special_chars=True):
    password_entry.delete(0, END)
    # Define character sets
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- Search Email & Password ------------------------------- #
def search_credentials():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not Found", message="No Data File Found")
    else:
        if website in data:
            email_data = data[website]["email"]
            password_data = data[website]["password"]
            messagebox.showinfo(title="Here are your credentials!", message=f"Your credentials for the Website {website} are:\n"
                                                                            f"Email: {email_data}\n"
                                                                            f"Password: {password_data}")
        else:
            messagebox.showinfo(title="No data found", message=f"We have not found any credentials for the Website {website}")
    finally:
        website_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def safe_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not email or not password:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")

    else:
        try:
            # Reading old data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # Create json file if no file exists
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            # Save updated data to json
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1,)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, string="sash.baschera@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=safe_data)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", command=search_credentials, width=13)
search_button.grid(column=2, row=1)

window.mainloop()
