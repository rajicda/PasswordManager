from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    if website_input.get() == "" or email_input.get() == "" or password_input.get() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(),
                                       message=f"These are the details entered: \nEmail: {email_input.get()}\nPassword: {password_input.get()}\nIs it ok to save?")

        if is_ok:
            data = f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n"
            with open("data.txt", "a") as file:
                file.write(data)
                website_input.delete(0, END)
            password_input.delete(0, END)


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

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(END, "test@test.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
