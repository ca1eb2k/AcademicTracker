import tkinter as tk
from tkinter import messagebox

def write_credentials(user_id, username, email, password):
    with open('logindetails.txt', 'a') as file:
        file.write(f'{user_id},{username},{email},{password}\n')

def check_credentials(username, password):
    with open('logindetails.txt', 'r') as file:
        for line in file:
            _, usr, _, pwd = line.strip().split(',')
            if usr == username and pwd == password:
                return True
        return False

def check_username_and_email(username, email):
    with open('logindetails.txt', 'r') as file:
        for line in file:
            _, usr, eml, _ = line.strip().split(',')
            if usr == username or eml == email:
                return True
        return False

def generate_user_id():
    try:
        with open('logindetails.txt', 'r') as file:
            last_line = list(file)[-1]
            last_id = int(last_line.strip().split(',')[0])
            return last_id + 1
    except (IndexError, FileNotFoundError):
        return 1

def validate_email(email):
    if '.' in email and '@' in email:
        return True
    else:
        return False

def signup():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if not validate_email(email):
        messagebox.showinfo("Error", "Invalid email.")
        return
    if check_username_and_email(username, email):
        messagebox.showinfo("Error", "Username or email is already in use.")
        return
    user_id = generate_user_id()
    write_credentials(user_id, username, email, password)
    signup_success_label.config(text="Sign-Up Success!")

def login():
    username = username_entry.get()
    password = password_entry.get()
    if check_credentials(username, password):
        success_window = tk.Toplevel()
        success_window.geometry("200x100")
        success_label = tk.Label(success_window, text="Success!")
        success_label.pack()
        success_window.after(2000, success_window.destroy)  # Close the window after 2 seconds
        root.destroy()  # Close the login window
        global_vars = globals()
        with open("menu.py") as file:  # Ensure menu.py is in the same directory
            exec(file.read(), global_vars)  # Run the menu.py script in global scope
    else:
        messagebox.showinfo("Error", "Wrong username or password")



root = tk.Tk()
root.title("AcademicTracker - Login")
root.iconbitmap("logo.ico")
root.geometry("1000x600")

username_label = tk.Label(root, text="Username")
username_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email")
email_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password")
password_entry = tk.Entry(root, show="*")

signup_button = tk.Button(root, text="Sign up", command=signup)
login_button = tk.Button(root, text="Log in", command=login)

username_label.pack()
username_entry.pack()

email_label.pack()
email_entry.pack()

password_label.pack()
password_entry.pack()

signup_button.pack()
login_button.pack()

signup_success_label = tk.Label(root, text="")
signup_success_label.pack()

root.mainloop()
