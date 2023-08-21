from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, messagebox
from random import choice, shuffle, randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_generated = "".join(password_list)
    password_input.insert(0, password_generated)
    pyperclip.copy(password_generated)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "Username": username,
            "Password": password,
        }
    }

    if (website == "") or (password == "") or (username == ""): 
        messagebox.showinfo(title="Alert", message="Please don't leave any fields empty!")
    else :
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername/Email: {username} \nPassword: {password}")

        if is_ok :
            try :
                with open('data.json', 'r') as datafile:
                    # reading old data
                    data = json.load(datafile)
            except FileNotFoundError :
                with open('data.json', 'w') as datafile:
                    # create data from scratch
                    json.dump(new_data, datafile, indent=4)
            else :
                # updating old data with new_data
                data.update(new_data)
                with open('data.json', 'w') as datafile:
                    # saving updated_data
                    json.dump(data, datafile, indent=4)
            finally :
                web_input.delete(0, 'end')
                username_input.delete(0, 'end')
                username_input.insert(0, '@gmail.com')
                password_input.delete(0, 'end')
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_input.get()
    try :
        with open('data.json', 'r') as datafile :
            data = json.load(datafile)
    except FileNotFoundError :
        messagebox.showerror(title='FileNotFound', message='Not such a file directory')
    else : 
        if website in data:
            username = data[website]['Username']
            password = data[website]['Password']
            messagebox.showinfo(title=website, message=f"Username: {username} \nPassword:{password}")
        else :
            messagebox.showinfo(title="Can't access information", message="No Details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


## Label
web_title = Label(text="Website:")
web_title.grid(row=1, column=0)

username_title = Label(text="Email/Username:")
username_title.grid(row=2, column=0)

password_title = Label(text="Password:")
password_title.grid(row=3, column=0)


## input
web_input = Entry(width=36)
web_input.grid(row=1, column=1)
web_input.focus()  # focusing the cursor

username_input = Entry(width=36)
username_input.grid(row=2, column=1)
username_input.insert(0, string="@gmail.com")

password_input = Entry(width=36)
password_input.grid(row=3, column=1)


## Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=15, command=save)
add_button.grid(row=4, column=1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()