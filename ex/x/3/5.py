import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


# Database Manager Class
class DatabaseManager:
    def __init__(self, db_name="student_management.db"):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute(
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
        self.conn.commit()

    def insert_student(self, name, age, gender, address):
        self.c.execute(
            "INSERT INTO students (name, age, gender, address) VALUES (?, ?, ?, ?)",
            (name, age, gender, address),
        )
        self.conn.commit()

    def update_student(self, student_id, name, age, gender, address):
        self.c.execute(
            "UPDATE students SET name=?, age=?, gender=?, address=? WHERE id=?",
            (name, age, gender, address, student_id),
        )
        self.conn.commit()

    def delete_student(self, student_id):
        self.c.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.conn.commit()

    def search_students(self, query):
        self.c.execute(
            "SELECT * FROM students WHERE name LIKE ? OR id LIKE ?",
            ("%" + query + "%", "%" + query + "%"),
        )
        return self.c.fetchall()

    def fetch_all_students(self):
        self.c.execute("SELECT * FROM students")
        return self.c.fetchall()

    def close(self):
        self.conn.close()


# Student Management App Class
class StudentManagementApp:
    def __init__(self, root):
        self.db = DatabaseManager()

        # Main Window
        self.root = root
        self.root.title("Student Management System")

        self.setup_ui()
        self.refresh_students()

    def setup_ui(self):
        frame = Frame(self.root)
        frame.pack(pady=20)

        Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky=E)
        Label(frame, text="Age").grid(row=1, column=0, padx=10, pady=5, sticky=E)
        Label(frame, text="Gender").grid(row=2, column=0, padx=10, pady=5, sticky=E)
        Label(frame, text="Address").grid(row=3, column=0, padx=10, pady=5, sticky=E)

        self.entry_name = Entry(frame, width=30)
        self.entry_name.grid(row=0, column=1, padx=20, pady=5)
        self.entry_age = Entry(frame, width=30)
        self.entry_age.grid(row=1, column=1, padx=20, pady=5)
        self.entry_gender = Entry(frame, width=30)
        self.entry_gender.grid(row=2, column=1, padx=20, pady=5)
        self.entry_address = Entry(frame, width=30)
        self.entry_address.grid(row=3, column=1, padx=20, pady=5)

        button_frame = Frame(self.root)
        button_frame.pack(pady=20)

        add_btn = Button(button_frame, text="Add Student", command=self.add_student)
        add_btn.grid(row=0, column=0, padx=10)

        update_btn = Button(
            button_frame, text="Update Student", command=self.update_student
        )
        update_btn.grid(row=0, column=1, padx=10)

        delete_btn = Button(
            button_frame, text="Delete Student", command=self.delete_student
        )
        delete_btn.grid(row=0, column=2, padx=10)

        load_btn = Button(button_frame, text="Load Student", command=self.load_student)
        load_btn.grid(row=0, column=3, padx=10)

        search_frame = Frame(self.root)
        search_frame.pack(pady=10)

        Label(search_frame, text="Search").grid(
            row=0, column=0, padx=10, pady=5, sticky=E
        )
        self.entry_search = Entry(search_frame, width=30)
        self.entry_search.grid(row=0, column=1, padx=20, pady=5)
        search_btn = Button(search_frame, text="Search", command=self.search_students)
        search_btn.grid(row=0, column=2, padx=10)

        listbox_frame = Frame(self.root)
        listbox_frame.pack(pady=10)

        columns = ("ID", "Name", "Age", "Gender", "Address")
        self.listbox = tTreeview(listbox_frame, columns=columns, show="headings")
        for col in columns:
            self.listbox.heading(col, text=col)
            self.listbox.column(col, width=100)

        self.listbox.pack(fill="both", expand=True)

    def clear_entries(self):
        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.entry_gender.delete(0, END)
        self.entry_address.delete(0, END)

    def refresh_students(self):
        self.listbox.delete(*self.listbox.get_children())
        students = self.db.fetch_all_students()
        for student in students:
            self.listbox.insert("", "end", values=student)

    def add_student(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.entry_gender.get()
        address = self.entry_address.get()

        if name and age and gender and address:
            self.db.insert_student(name, age, gender, address)
            self.refresh_students()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def update_student(self):
        selected = self.listbox.selection()
        if not selected:
            messagebox.showwarning(
                "Selection Error", "Please select a student to update."
            )
            return

        name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.entry_gender.get()
        address = self.entry_address.get()

        if name and age and gender and address:
            student_id = self.listbox.item(selected[0])["values"][0]
            self.db.update_student(student_id, name, age, gender, address)
            self.refresh_students()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def delete_student(self):
        selected = self.listbox.selection()
        if not selected:
            messagebox.showwarning(
                "Selection Error", "Please select a student to delete."
            )
            return

        student_id = self.listbox.item(selected[0])["values"][0]
        self.db.delete_student(student_id)
        self.refresh_students()

    def search_students(self):
        query = self.entry_search.get()
        self.listbox.delete(*self.listbox.get_children())

        students = self.db.search_students(query)
        for student in students:
            self.listbox.insert("", "end", values=student)

    def load_student(self):
        selected = self.listbox.selection()
        if not selected:
            messagebox.showwarning(
                "Selection Error", "Please select a student to load."
            )
            return

        student = self.listbox.item(selected[0])["values"]
        self.clear_entries()
        self.entry_name.insert(END, student[1])
        self.entry_age.insert(END, student[2])
        self.entry_gender.insert(END, student[3])
        self.entry_address.insert(END, student[4])


# Main loop
if __name__ == "__main__":
    root = Tk()
    app = StudentManagementApp(root)
    root.mainloop()
