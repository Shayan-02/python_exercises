import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
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


# Main Application Class
class TodoListApp(Tk):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.title("Advanced To-Do List App")
        self.geometry("800x600")
        self.configure(bg="#F0F0F0")  # Light gray background

        self.setup_ui()

    def setup_ui(self):
        # Header Frame
        header_frame = Frame(self, bg="#3498DB")  # Blue background
        header_frame.pack(fill=X, pady=10)
        Label(
            header_frame,
            text="To-Do List App",
            font=("Helvetica", 20),
            bg="#3498DB",
            fg="#FFFFFF",
        ).pack()

        # Filter and Sort Controls
        control_frame = Frame(self, bg="#F0F0F0")
        control_frame.pack(fill=X, pady=10)

        self.filter_combo = tCombobox(
            control_frame, values=["All", "Pending", "Completed"], state="readonly"
        )
        self.filter_combo.set("All")
        self.filter_combo.grid(row=0, column=0, padx=10)
        self.filter_combo.bind("<<ComboboxSelected>>", self.refresh_tasks)

        self.sort_combo = tCombobox(
            control_frame, values=["Priority", "Due Date"], state="readonly"
        )
        self.sort_combo.set("Priority")
        self.sort_combo.grid(row=0, column=1, padx=10)
        self.sort_combo.bind("<<ComboboxSelected>>", self.refresh_tasks)

        # Task Table
        self.table = tTreeview(
            self,
            columns=("ID", "Title", "Priority", "Due Date", "Status"),
            show="headings",
        )
        self.table.heading("ID", text="ID")
        self.table.heading("Title", text="Title")
        self.table.heading("Priority", text="Priority")
        self.table.heading("Due Date", text="Due Date")
        self.table.heading("Status", text="Status")
        self.table.column("ID", width=50)
        self.table.column("Title", width=200)
        self.table.column("Priority", width=100)
        self.table.column("Due Date", width=150)
        self.table.column("Status", width=100)
        self.table.pack(fill=BOTH, expand=True)

        # Action Buttons
        button_frame = Frame(self, bg="#F0F0F0")
        button_frame.pack(pady=10)

        add_btn = Button(
            button_frame,
            text="Add Task",
            command=self.add_task,
            bg="#2ECC71",
            fg="#FFFFFF",
        )  # Green button
        add_btn.grid(row=0, column=0, padx=5)
        update_btn = Button(
            button_frame,
            text="Update Task",
            command=self.update_task,
            bg="#F39C12",
            fg="#FFFFFF",
        )  # Orange button
        update_btn.grid(row=0, column=1, padx=5)
        delete_btn = Button(
            button_frame,
            text="Delete Task",
            command=self.delete_task,
            bg="#E74C3C",
            fg="#FFFFFF",
        )  # Red button
        delete_btn.grid(row=0, column=2, padx=5)
        complete_btn = Button(
            button_frame,
            text="Mark Completed",
            command=self.mark_completed,
            bg="#3498DB",
            fg="#FFFFFF",
        )  # Blue button
        complete_btn.grid(row=0, column=3, padx=5)

        self.refresh_tasks()

    def refresh_tasks(self, event=None):
        filter_status = (
            None if self.filter_combo.get() == "All" else self.filter_combo.get()
        )
        sort_by = "priority" if self.sort_combo.get() == "Priority" else "due_date"

        for item in self.table.get_children():
            self.table.delete(item)

        tasks = self.db.fetch_tasks(filter_status=filter_status, sort_by=sort_by)
        for task in tasks:
            self.table.insert("", "end", values=task)

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Task Title:")
        priority = simpledialog.askinteger("Add Task", "Priority (1-5):")
        due_date = simpledialog.askstring("Add Task", "Due Date (YYYY-MM-DD):")

        if title and priority and due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
                if priority < 1 or priority > 5:
                    raise ValueError
                self.db.insert_task(title, priority, due_date)
                self.refresh_tasks()
            except ValueError:
                messagebox.showerror(
                    "Input Error",
                    "Priority must be an integer between 1 and 5. Due Date must be in YYYY-MM-DD format.",
                )
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def update_task(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
            return

        task_id = self.table.item(selected_item[0])["values"][0]
        task = [item for item in self.table.item(selected_item[0])["values"]]
        task = (task_id, *task[1:])

        title = simpledialog.askstring(
            "Update Task", "Task Title:", initialvalue=task[1]
        )
        priority = simpledialog.askinteger(
            "Update Task", "Priority (1-5):", initialvalue=task[2]
        )
        due_date = simpledialog.askstring(
            "Update Task", "Due Date (YYYY-MM-DD):", initialvalue=task[3]
        )
        status = (
            "Completed"
            if messagebox.askyesno("Update Task", "Mark task as completed?")
            else "Pending"
        )

        if title and priority and due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
                if priority < 1 or priority > 5:
                    raise ValueError
                self.db.update_task(task_id, title, priority, due_date, status)
                self.refresh_tasks()
            except ValueError:
                messagebox.showerror(
                    "Input Error",
                    "Priority must be an integer between 1 and 5. Due Date must be in YYYY-MM-DD format.",
                )
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def delete_task(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
            return

        task_id = self.table.item(selected_item[0])["values"][0]
        self.db.delete_task(task_id)
        self.refresh_tasks()

    def mark_completed(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning(
                "Selection Error", "Please select a task to mark as completed."
            )
            return

        task_id = self.table.item(selected_item[0])["values"][0]
        task = [item for item in self.table.item(selected_item[0])["values"]]
        self.db.update_task(task_id, task[1], task[2], task[3], "Completed")
        self.refresh_tasks()

    def on_closing(self):
        self.db.close()
        self.destroy()


# Main loop
if __name__ == "__main__":
    app = TodoListApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
