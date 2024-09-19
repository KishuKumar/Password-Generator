from tkinter import *
from tkinter import messagebox
from passwordMaker import new_password
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def clear():
    website_input.delete(0, END)
    password_input.delete(0, END)

def paste():
    password_input.delete(0, END)
    password = "".join(new_password())
    password_input.insert(0, password)
    pyperclip.copy(password)


def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="JSON file was not found.")
    else:
        if len(website) == 0:
            messagebox.showerror(title="Empty Field", message="Website field can't be empty.")
        elif website in data:
            messagebox.showinfo(title=website, message=f"Email/Username: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Data not Found", message=f"No matching data found for {website}.")
    finally:
        clear()

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
            "email": email,
            "password": password
        },
    }
    if len(website) == 0 and len(password) == 0:
        messagebox.showerror(title="Invalid Info", message="Website or Password can't be empty!")
    else:
        you_sure = messagebox.askokcancel(title=website, message=f"Email/Username: {email}\n"
                                                                 f"Password: {password}\n"
                                                                 f"Proceed with this info?")
        if you_sure:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                clear()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1, sticky="EW")

search_button = Button(text=" Search ", command=search)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.insert(0, "kumarkishu749@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

generate_button = Button(text="Generate", command=paste)
generate_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
