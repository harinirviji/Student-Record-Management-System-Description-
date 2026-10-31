import tkinter as tk
import json
import os

students = []

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    department = dept_entry.get()

    if name and roll and department:
        student = {
            "Name": name,
            "Roll Number": roll,
            "Department": department
        }

        students.append(student)
        save_data()
        status.config(text="Student added successfully!")

        clear_fields()
    else:
        status.config(text="Please fill all fields")

def search_student():
    roll = roll_entry.get()

    for student in students:
        if student["Roll Number"] == roll:
            status.config(
                text=f"Name: {student['Name']}, "
                     f"Department: {student['Department']}"
            )
            return

    status.config(text="Student not found")

def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Student Management System")
root.geometry("450x400")

tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 18, "bold")
).pack(pady=15)

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Department").pack()
dept_entry = tk.Entry(root)
dept_entry.pack()

tk.Button(root, text="Add Student",
          command=add_student).pack(pady=8)

tk.Button(root, text="Search Student",
          command=search_student).pack()

tk.Button(root, text="Clear",
          command=clear_fields).pack(pady=8)

status = tk.Label(root, text="")
status.pack()

root.mainloop()
