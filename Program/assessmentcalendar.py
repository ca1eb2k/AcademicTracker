from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import datetime
import json

# Create the root window
root = Tk()
root.geometry("1000x600")
root.title("Assessment Calendar")

# Function to load assessments from file
def load_assessments_from_file():
    try:
        with open('assessmentinfo.txt', 'r') as f:
            assessments_str = f.read()
            return json.loads(assessments_str)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Load assessments from file
assessments = load_assessments_from_file()

# Create a listbox to display upcoming assessments
assessment_listbox = Listbox(root, width=50)
assessment_listbox.pack(pady=20)

def save_assessments_to_file():
    # Convert assessments to a JSON string
    assessments_str = json.dumps(assessments)
    # Write the JSON string to a file
    with open('assessmentinfo.txt', 'w') as f:
        f.write(assessments_str)

def update_assessment_list():
    # Clear the listbox
    assessment_listbox.delete(0, END)
    # Sort the assessments by date
    sorted_assessments = sorted(assessments.items(), key=lambda x: datetime.datetime.strptime(x[0], "%m/%d/%y"))
    # Add each assessment to the listbox
    for date, assessment in sorted_assessments:
        assessment_listbox.insert(END, f"{date}: {assessment}")
    # Save assessments to file
    save_assessments_to_file()

# Update the list of assessments right after loading them
update_assessment_list()

def add_assessment():
    # Get the selected date
    selected_date = cal.get_date()
    # Get the assessment data from the user
    assessment = assessment_entry.get()
    if assessment:  # Check that the assessment isn't empty
        # Add the assessment to the dictionary, associated with the selected date
        assessments[selected_date] = assessment
        # Display a success message
        messagebox.showinfo("Success", f"Assessment for {selected_date} added successfully!")
        # Update the list of assessments
        update_assessment_list()
        # Clear the assessment entry field
        assessment_entry.delete(0, 'end')
    else:
        messagebox.showinfo("Error", "Please enter an assessment!")

# Create a calendar
cal = Calendar(root, selectmode="day", year=2023, month=7, day=14)
cal.pack(pady=20)

# Create a label for the assessment entry
assessment_label = Label(root, text="Enter your assessment here:")
assessment_label.pack(pady=10)

# Create a text entry to input assessment
assessment_entry = Entry(root, width=50)
assessment_entry.pack(pady=20)

# Create a button to add assessment
add_button = Button(root, text="Add Assessment", command=add_assessment)
add_button.pack()

# Start the application
root.mainloop()
