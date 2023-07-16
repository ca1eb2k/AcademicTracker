import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Button, PhotoImage, Label, font
import json

class TimetableApp:

    def __init__(self, master):
        self.master = master
        self.master.title("AcademicTracker - Timetable")
        self.master.geometry("1000x600")  
        self.master.iconbitmap("logo.ico")

        self.days = ["Day {}".format(i) for i in range(1, 11)]
        self.subjects = ["Subject {}".format(i) for i in range(1, 6)]

        self.entries = {}
        self.data_file = "timetableinfo.txt"

        # Create labels for days and entries for subjects
        for i in range(10):
            tk.Label(master, text=self.days[i], width=8).grid(row=0, column=i+1, padx=5)  # Adjusted width and added padx for column spacing
            for j in range(5):
                if i == 0:
                    tk.Label(master, text=self.subjects[j], width=10).grid(row=j+1, column=0, pady=5)  # Adjusted width and added pady for row spacing
                self.entries[(i, j)] = tk.Entry(master, width=10)  # Adjusted width of the Entry widget
                self.entries[(i, j)].grid(row=j+1, column=i+1, padx=5)  # Added padx for column spacing

        # Load existing data
        self.load_data()

        # Save button
        save_button = tk.Button(master, text="Save", command=self.save_data)
        save_button.grid(row=6, column=0, columnspan=11, pady=10)  # Added pady for button spacing

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)

            for key, value in data.items():
                key = key.replace("(", "")
                key = key.replace(")", "")
                i, j = map(int, key.split(","))
                self.entries[(i, j)].insert(0, value)

        except FileNotFoundError:
            pass  # It's okay if the file doesn't exist yet

        except json.JSONDecodeError:
            pass  # It's okay if the file is empty

    def save_data(self):
        data = {str(key): entry.get() for key, entry in self.entries.items()}

        with open(self.data_file, 'w') as f:
            json.dump(data, f)

        messagebox.showinfo("Saved", "Your timetable has been saved!")


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = TimetableApp(root)
    root.mainloop()
