import tkinter as tk
from datetime import datetime, timedelta
import json

class HomeworkJournal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Homework Journal")
        self.geometry("1000x600")

        self.current_date = datetime.now()

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side="top", fill="x")

        self.left_button = tk.Button(self.button_frame, text="<", command=self.previous_week)
        self.left_button.pack(side="left")

        self.right_button = tk.Button(self.button_frame, text=">", command=self.next_week)
        self.right_button.pack(side="right")

        self.homework_frame = tk.Frame(self)
        self.homework_frame.pack(side="top", fill="both", expand=True)

        self.data = self.load_data()
        self.entries = {}
        self.checks = {}

        self.populate_week()

    def load_data(self):
        try:
            with open("homeworkinfo.txt", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}


    def save_data(self):
        with open("homeworkinfo.txt", "w") as f:
            json.dump(self.data, f)

    def populate_week(self):
        for widget in self.homework_frame.winfo_children():
            widget.destroy()

        subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
        for i in range(5):
            subject_label = tk.Label(self.homework_frame, text=subjects[i])
            subject_label.grid(row=0, column=i+1, sticky="w")
        complete_label = tk.Label(self.homework_frame, text="Complete")
        complete_label.grid(row=0, column=6, sticky="w", columnspan=5)

        for i in range(1, 8):
            date = (self.current_date + timedelta(days=i-1)).strftime("%Y-%m-%d")
            date_label = tk.Label(self.homework_frame, text=date)
            date_label.grid(row=i, column=0, sticky="w")

            self.entries[date] = {}
            self.checks[date] = {}
            for j in range(1, 6):
                text_var = tk.StringVar()
                text_var.set(self.data.get(date, {}).get(subjects[j-1], ("", False))[0])

                entry = tk.Entry(self.homework_frame, textvariable=text_var, width=20)
                entry.grid(row=i, column=j, sticky="w")

                check_var = tk.BooleanVar()
                check_var.set(self.data.get(date, {}).get(subjects[j-1], ("", False))[1])
                check_button = tk.Checkbutton(self.homework_frame, variable=check_var)
                check_button.grid(row=i, column=j+5, sticky="w")

                self.entries[date][subjects[j-1]] = text_var
                self.checks[date][subjects[j-1]] = check_var

    def previous_week(self):
        self.save_week()
        self.current_date -= timedelta(weeks=1)
        self.populate_week()

    def next_week(self):
        self.save_week()
        self.current_date += timedelta(weeks=1)
        self.populate_week()

    def save_week(self):
        for date, subjects in self.entries.items():
            for subject, text_var in subjects.items():
                homework = text_var.get()
                complete = self.checks[date][subject].get()
                if date not in self.data:
                    self.data[date] = {}
                self.data[date][subject] = (homework, complete)
        self.save_data()

if __name__ == "__main__":
    app = HomeworkJournal()
    app.mainloop()
