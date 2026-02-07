import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

# Database setup
conn = sqlite3.connect("student_management.db")
c = conn.cursor()

c.execute(
    """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    address TEXT
)
"""
)
conn.commit()


# Functions
def refresh_students():
    listbox.delete(*listbox.get_children())
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    for student in students:
        listbox.insert("", "end", values=student)


def add_student():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    address = entry_address.get()

    if name and age and gender and address:
        c.execute(
            "INSERT INTO students (name, age, gender, address) VALUES (?, ?, ?, ?)",
            (name, age, gender, address),
        )
        conn.commit()
        refresh_students()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required.")


def update_student():
    selected = listbox.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a student to update.")
        return

    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    address = entry_address.get()

    if name and age and gender and address:
        student_id = listbox.item(selected[0])["values"][0]
        c.execute(
            "UPDATE students SET name=?, age=?, gender=?, address=? WHERE id=?",
            (name, age, gender, address, student_id),
        )
        conn.commit()
        refresh_students()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required.")


def delete_student():
    selected = listbox.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a student to delete.")
        return

    student_id = listbox.item(selected[0])["values"][0]
    c.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    refresh_students()


def search_students():
    query = entry_search.get()
    listbox.delete(*listbox.get_children())

    c.execute(
        "SELECT * FROM students WHERE name LIKE ? OR id LIKE ?",
        ("%" + query + "%", "%" + query + "%"),
    )
    students = c.fetchall()
    for student in students:
        listbox.insert("", "end", values=student)


def load_student():
    selected = listbox.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a student to load.")
        return

    student = listbox.item(selected[0])["values"]
    clear_entries()
    entry_name.insert(END, student[1])
    entry_age.insert(END, student[2])
    entry_gender.insert(END, student[3])
    entry_address.insert(END, student[4])


def clear_entries():
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_gender.delete(0, END)
    entry_address.delete(0, END)


# GUI Layout
root = Tk()
root.title("Student Management System")

frame = Frame(root)
frame.pack(pady=20)

Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky=E)
Label(frame, text="Age").grid(row=1, column=0, padx=10, pady=5, sticky=E)
Label(frame, text="Gender").grid(row=2, column=0, padx=10, pady=5, sticky=E)
Label(frame, text="Address").grid(row=3, column=0, padx=10, pady=5, sticky=E)

entry_name = Entry(frame, width=30)
entry_name.grid(row=0, column=1, padx=20, pady=5)
entry_age = Entry(frame, width=30)
entry_age.grid(row=1, column=1, padx=20, pady=5)
entry_gender = Entry(frame, width=30)
entry_gender.grid(row=2, column=1, padx=20, pady=5)
entry_address = Entry(frame, width=30)
entry_address.grid(row=3, column=1, padx=20, pady=5)

button_frame = Frame(root)
button_frame.pack(pady=20)

add_btn = Button(button_frame, text="Add Student", command=add_student)
add_btn.grid(row=0, column=0, padx=10)

update_btn = Button(button_frame, text="Update Student", command=update_student)
update_btn.grid(row=0, column=1, padx=10)

delete_btn = Button(button_frame, text="Delete Student", command=delete_student)
delete_btn.grid(row=0, column=2, padx=10)

load_btn = Button(button_frame, text="Load Student", command=load_student)
load_btn.grid(row=0, column=3, padx=10)

search_frame = Frame(root)
search_frame.pack(pady=10)

Label(search_frame, text="Search").grid(row=0, column=0, padx=10, pady=5, sticky=E)
entry_search = Entry(search_frame, width=30)
entry_search.grid(row=0, column=1, padx=20, pady=5)
search_btn = Button(search_frame, text="Search", command=search_students)
search_btn.grid(row=0, column=2, padx=10)

listbox_frame = Frame(root)
listbox_frame.pack(pady=10)

columns = ("ID", "Name", "Age", "Gender", "Address")
listbox = tTreeview(listbox_frame, columns=columns, show="headings")
for col in columns:
    listbox.heading(col, text=col)
    listbox.column(col, width=100)

listbox.pack(fill="both", expand=True)

refresh_students()

root.mainloop()
