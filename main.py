import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    new_data = {website_input.get():
                    {"email": email_input.get(),
                     "password": password_input.get()}}
    if website_input.get() == "" or email_input.get() == "" or password_input.get() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w+") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
        # pandas.DataFrame().to_json()
        # old_data = pandas.read_json("data.json")
        # data = {website_input.get():
        #         {"Email": email_input.get(),
        #          "Password": password_input.get()}}
        # data = pandas.DataFrame(data)
        # new_data = pandas.concat([old_data, data])
        # new_data.to_json("data.json", indent=4)


# ---------------------------- SEARCH DATA ------------------------------- #


def search_website():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No Data File Found.")
    else:
        if website_input.get() in data:
            website_data = data[website_input.get()]
            messagebox.showinfo(title=website_input.get(), message=f"Email: {website_data['email']}\nPassword: "
                                                                f"{website_data['password']}")
        else:
            messagebox.showinfo(title="ERROR", message=f"No details for the {website_input.get()} exists.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(END, "test@test.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search_website, width=13)
search_button.grid(row=1, column=2)


window.mainloop()
