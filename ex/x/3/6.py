import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime


# Database Manager Class
class DatabaseManager:
    def __init__(self, db_name="todolist.db"):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute(
            """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            priority INTEGER,
            due_date TEXT,
            status TEXT
        )
        """
        )
        self.conn.commit()

    def insert_task(self, title, priority, due_date, status="Pending"):
        self.c.execute(
            "INSERT INTO tasks (title, priority, due_date, status) VALUES (?, ?, ?, ?)",
            (title, priority, due_date, status),
        )
        self.conn.commit()

    def update_task(self, task_id, title, priority, due_date, status):
        self.c.execute(
            "UPDATE tasks SET title=?, priority=?, due_date=?, status=? WHERE id=?",
            (title, priority, due_date, status, task_id),
        )
        self.conn.commit()

    def delete_task(self, task_id):
        self.c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.conn.commit()

    def fetch_tasks(self, filter_status=None, sort_by=None):
        query = "SELECT * FROM tasks"
        conditions = []
        if filter_status:
            conditions.append(f"status='{filter_status}'")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        if sort_by:
            query += f" ORDER BY {sort_by}"

        self.c.execute(query)
        return self.c.fetchall()

    def close(self):
        self.conn.close()


# To-Do List App Class
class TodoListApp:
    def __init__(self, root):
        self.db = DatabaseManager()

        # Main Window
        self.root = root
        self.root.title("Advanced To-Do List App")

        self.setup_ui()
        self.refresh_tasks()

    def setup_ui(self):
        frame = Frame(self.root)
        frame.pack(pady=20)

        Label(frame, text="Task Title").grid(row=0, column=0, padx=10, pady=5, sticky=E)
        Label(frame, text="Priority (1-5)").grid(
            row=1, column=0, padx=10, pady=5, sticky=E
        )
        Label(frame, text="Due Date (YYYY-MM-DD)").grid(
            row=2, column=0, padx=10, pady=5, sticky=E
        )

        self.entry_title = Entry(frame, width=30)
        self.entry_title.grid(row=0, column=1, padx=20, pady=5)
        self.entry_priority = Entry(frame, width=30)
        self.entry_priority.grid(row=1, column=1, padx=20, pady=5)
        self.entry_due_date = Entry(frame, width=30)
        self.entry_due_date.grid(row=2, column=1, padx=20, pady=5)

        button_frame = Frame(self.root)
        button_frame.pack(pady=20)

        add_btn = Button(button_frame, text="Add Task", command=self.add_task)
        add_btn.grid(row=0, column=0, padx=10)

        update_btn = Button(button_frame, text="Update Task", command=self.update_task)
        update_btn.grid(row=0, column=1, padx=10)

        delete_btn = Button(button_frame, text="Delete Task", command=self.delete_task)
        delete_btn.grid(row=0, column=2, padx=10)

        load_btn = Button(button_frame, text="Load Task", command=self.load_task)
        load_btn.grid(row=0, column=3, padx=10)

        mark_completed_btn = Button(
            button_frame, text="Mark Completed", command=self.mark_completed
        )
        mark_completed_btn.grid(row=0, column=4, padx=10)

        filter_frame = Frame(self.root)
        filter_frame.pack(pady=10)

        Label(filter_frame, text="Filter By:").grid(row=0, column=0, padx=10, pady=5)
        self.filter_var = StringVar(value="All")
        filter_options = ["All", "Pending", "Completed"]
        filter_menu = OptionMenu(
            filter_frame, self.filter_var, *filter_options, command=self.refresh_tasks
        )
        filter_menu.grid(row=0, column=1, padx=10)

        Label(filter_frame, text="Sort By:").grid(row=0, column=2, padx=10, pady=5)
        self.sort_var = StringVar(value="priority")
        sort_options = ["priority", "due_date"]
        sort_menu = OptionMenu(
            filter_frame, self.sort_var, *sort_options, command=self.refresh_tasks
        )
        sort_menu.grid(row=0, column=3, padx=10)

        listbox_frame = Frame(self.root)
        listbox_frame.pack(pady=10)

        columns = ("ID", "Title", "Priority", "Due Date", "Status")
        self.listbox = tTreeview(listbox_frame, columns=columns, show="headings")
        for col in columns:
            self.listbox.heading(col, text=col)
            self.listbox.column(col, width=100)

        self.listbox.pack(fill="both", expand=True)

    def clear_entries(self):
        self.entry_title.delete(0, END)
        self.entry_priority.delete(0, END)
        self.entry_due_date.delete(0, END)

    def refresh_tasks(self, *args):
        filter_status = (
            None if self.filter_var.get() == "All" else self.filter_var.get()
        )
        sort_by = self.sort_var.get()

        self.listbox.delete(*self.listbox.get_children())
        tasks = self.db.fetch_tasks(filter_status=filter_status, sort_by=sort_by)
        for task in tasks:
            self.listbox.insert("", "end", values=task)

    def add_task(self):
        title = self.entry_title.get()
        priority = self.entry_priority.get()
        due_date = self.entry_due_date.get()

        if title and priority and due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")  # Validate date format
                priority = int(priority)
                if priority < 1 or priority > 5:
                    raise ValueError

                self.db.insert_task(title, priority, due_date)
                self.refresh_tasks()
                self.clear_entries()
            except ValueError:
                messagebox.showwarning(
                    "Input Error",
                    "Priority must be an integer between 1 and 5. Due Date must be in YYYY-MM-DD format.",
                )
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def update_task(self):
        selected = self.listbox.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
            return

        title = self.entry_title.get()
        priority = self.entry_priority.get()
        due_date = self.entry_due_date.get()

        if title and priority and due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
                priority = int(priority)
                if priority < 1 or priority > 5:
                    raise ValueError

                task_id = self.listbox.item(selected[0])["values"][0]
                status = self.listbox.item(selected[0])["values"][4]
                self.db.update_task(task_id, title, priority, due_date, status)
                self.refresh_tasks()
                self.clear_entries()
            except ValueError:
                messagebox.showwarning(
                    "Input Error",
                    "Priority must be an integer between 1 and 5. Due Date must be in YYYY-MM-DD format.",
                )
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def delete_task(self):
        selected = self.listbox.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
            return

        task_id = self.listbox.item(selected[0])["values"][0]
        self.db.delete_task(task_id)
        self.refresh_tasks()

    def load_task(self):
        selected = self.listbox.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to load.")
            return

        task = self.listbox.item(selected[0])["values"]
        self.clear_entries()
        self.entry_title.insert(END, task[1])
        self.entry_priority.insert(END, task[2])
        self.entry_due_date.insert(END, task[3])

    def mark_completed(self):
        selected = self.listbox.selection()
        if not selected:
            messagebox.showwarning(
                "Selection Error", "Please select a task to mark as completed."
            )
            return

        task_id = self.listbox.item(selected[0])["values"][0]
        title = self.listbox.item(selected[0])["values"][1]
        priority = self.listbox.item(selected[0])["values"][2]
        due_date = self.listbox.item(selected[0])["values"][3]
        status = "Completed"
        self.db.update_task(task_id, title, priority, due_date, status)
        self.refresh_tasks()


# Main loop
if __name__ == "__main__":
    root = Tk()
    app = TodoListApp(root)
    root.mainloop()
