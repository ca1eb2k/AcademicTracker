import os
import subprocess
from tkinter import Tk, Button, PhotoImage, Label, font

def open_program(file_path):
    subprocess.call(['python', file_path])

root = Tk()
root.geometry("1000x600")
root.title("AcademicTracker - Home")
root.iconbitmap("logo.ico")

# Add welcome label
welcome_label = Label(root, text="Welcome to AcademicTracker!", font=("Arial", 36))
welcome_label.grid(row=0, column=0, columnspan=7, pady=20)

img1 = PhotoImage(file="calendar.png")
img2 = PhotoImage(file="timetable.png")
img3 = PhotoImage(file="homework.png")

button1 = Button(root, image=img1, command=lambda: open_program("assessmentcalendar.py"))
button2 = Button(root, image=img2, command=lambda: open_program("timetable.py"))
button3 = Button(root, image=img3, command=lambda: open_program("homework.py"))

# Get the width and height of the images
img_width = img1.width()
img_height = img1.height()

# Compute the starting x and y coordinates for the buttons
start_x = (1000 - 3*img_width - 2*20) // 2  # width of window - total width of buttons and gaps, all divided by 2
start_y = (600 - img_height) // 2  # height of window - height of button, all divided by 2

root.grid_columnconfigure(1, minsize=start_x)
root.grid_columnconfigure(2, minsize=img_width)
root.grid_columnconfigure(3, minsize=20)  # Gap
root.grid_columnconfigure(4, minsize=img_width)
root.grid_columnconfigure(5, minsize=20)  # Gap
root.grid_columnconfigure(6, minsize=img_width)
root.grid_rowconfigure(1, minsize=start_y)
root.grid_rowconfigure(2, minsize=img_height)

button1.grid(row=1, column=2)
button2.grid(row=1, column=4)
button3.grid(row=1, column=6)

root.mainloop()
