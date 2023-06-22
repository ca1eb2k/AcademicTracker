import tkinter as tk
from tkinter import ttk

TIMETABLE_FILE = "timetable_database.txt"

def open_timetable():
    timetable_window = tk.Toplevel(root)
    timetable_window.title("Timetable")

    timetable_data = []
    entries = []

    for i in range(5):
        row_entries = []
        for j in range(10):
            cell_entry = ttk.Entry(timetable_window)
            cell_entry.grid(row=i, column=j, padx=5, pady=5)
            row_entries.append(cell_entry)
        entries.append(row_entries)

    def save_timetable():
        for i in range(6):
            for j in range(10):
                timetable_data[i][j] = entries[i][j].get()

        with open(TIMETABLE_FILE, "w") as file:
            for row in timetable_data:
                line = "\t".join(row) + "\n"
                file.write(line)

        print("Timetable saved successfully!")

    style = ttk.Style()
    style.configure("Custom.TButton",
                    background="#E5EFC1",
                    foreground="black",
                    font=('Helvetica', 15),
                    borderwidth='1')
    style.map("Custom.TButton",
              foreground=[('pressed', 'yellow'),
                          ('active', 'green')],
              background=[('pressed', '!disabled', 'black'),
                          ('active', '#E5EFC1')])

    save_button = ttk.Button(timetable_window, text="Save", command=save_timetable, style="Custom.TButton")
    save_button.grid(row=6, columnspan=10, padx=5, pady=10)

    timetable_data = [['' for _ in range(10)] for _ in range(6)]

    try:
        with open(TIMETABLE_FILE, "r") as file:
            for i, line in enumerate(file):
                row_data = line.strip().split("\t")
                for j, data in enumerate(row_data):
                    timetable_data[i][j] = data
                    entries[i][j].insert(0, data)
    except FileNotFoundError:
        print("No existing timetable data found.")

root = tk.Tk()
root.title("My Planner")

image_path = "timetable.png"  # Replace with your image path
image = tk.PhotoImage(file=image_path)

style = ttk.Style()
style.configure("Custom.TButton",
                background="#E5EFC1",
                foreground="black",
                font=('Helvetica', 15),
                borderwidth='1')
style.map("Custom.TButton",
          foreground=[('pressed', 'yellow'),
                      ('active', 'green')],
          background=[('pressed', '!disabled', 'black'),
                      ('active', 'white')])

timetable_button = tk.Button(root, image=image, command=open_timetable, borderwidth=0) # use tk.Button instead of ttk.Button and set borderwidth to 0
timetable_button.image = image
timetable_button.pack(pady=10)

homework_button = ttk.Button(root, text="My Homework", style="Custom.TButton")
homework_button.pack(pady=10)

exams_button = ttk.Button(root, text="My Exams", style="Custom.TButton")
exams_button.pack(pady=10)

root.mainloop()
