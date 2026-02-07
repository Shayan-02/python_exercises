import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
)
from PyQt5.QtCore import Qt
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

    def fetch_all_tasks(self):
        self.c.execute("SELECT * FROM tasks")
        return self.c.fetchall()

    def close(self):
        self.conn.close()


# To-Do List App Class
class TodoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Input Fields
        form_layout = QHBoxLayout()
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Task Title")
        self.priority_input = QLineEdit(self)
        self.priority_input.setPlaceholderText("Priority (1-5)")
        self.due_date_input = QLineEdit(self)
        self.due_date_input.setPlaceholderText("Due Date (YYYY-MM-DD)")

        form_layout.addWidget(QLabel("Title:"))
        form_layout.addWidget(self.title_input)
        form_layout.addWidget(QLabel("Priority:"))
        form_layout.addWidget(self.priority_input)
        form_layout.addWidget(QLabel("Due Date:"))
        form_layout.addWidget(self.due_date_input)

        layout.addLayout(form_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add Task", self)
        add_btn.clicked.connect(self.add_task)
        update_btn = QPushButton("Update Task", self)
        update_btn.clicked.connect(self.update_task)
        delete_btn = QPushButton("Delete Task", self)
        delete_btn.clicked.connect(self.delete_task)
        complete_btn = QPushButton("Mark Completed", self)
        complete_btn.clicked.connect(self.mark_completed)

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(update_btn)
        btn_layout.addWidget(delete_btn)
        btn_layout.addWidget(complete_btn)

        layout.addLayout(btn_layout)

        # Task Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Title", "Priority", "Due Date", "Status"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.refresh_table()

        layout.addWidget(self.table)

        self.setLayout(layout)

    def refresh_table(self):
        self.table.setRowCount(0)
        tasks = self.db.fetch_all_tasks()
        for task in tasks:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for col, data in enumerate(task):
                self.table.setItem(row_position, col, QTableWidgetItem(str(data)))

    def add_task(self):
        title = self.title_input.text()
        priority = self.priority_input.text()
        due_date = self.due_date_input.text()

        if title and priority and due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")  # Validate date format
                priority = int(priority)
                if priority < 1 or priority > 5:
                    raise ValueError

                self.db.insert_task(title, priority, due_date)
                self.refresh_table()
                self.clear_inputs()
            except ValueError:
                QMessageBox.warning(
                    self,
                    "Input Error",
                    "Priority must be an integer between 1 and 5. Due Date must be in YYYY-MM-DD format.",
                )
        else:
            QMessageBox.warning(self, "Input Error", "All fields are required.")

    def update_task(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(
                self, "Selection Error", "Please select a task to update."
            )
            return

        task_id = int(self.table.item(selected, 0).text())
        title = self.title_input.text()
        priority = self.priority_input.text()
        due_date = self.due_date_input.text()

        if title and priority and due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
                priority = int(priority)
                if priority < 1 or priority > 5:
                    raise ValueError

                status = self.table.item(selected, 4).text()
                self.db.update_task(task_id, title, priority, due_date, status)
                self.refresh_table()
                self.clear_inputs()
            except ValueError:
                QMessageBox.warning(
                    self,
                    "Input Error",
                    "Priority must be an integer between 1 and 5. Due Date must be in YYYY-MM-DD format.",
                )
        else:
            QMessageBox.warning(self, "Input Error", "All fields are required.")

    def delete_task(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(
                self, "Selection Error", "Please select a task to delete."
            )
            return

        task_id = int(self.table.item(selected, 0).text())
        self.db.delete_task(task_id)
        self.refresh_table()

    def mark_completed(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(
                self, "Selection Error", "Please select a task to mark as completed."
            )
            return

        task_id = int(self.table.item(selected, 0).text())
        title = self.table.item(selected, 1).text()
        priority = self.table.item(selected, 2).text()
        due_date = self.table.item(selected, 3).text()
        status = "Completed"
        self.db.update_task(task_id, title, priority, due_date, status)
        self.refresh_table()

    def clear_inputs(self):
        self.title_input.clear()
        self.priority_input.clear()
        self.due_date_input.clear()

    def closeEvent(self, event):
        self.db.close()
        event.accept()


# Main loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoListApp()
    window.show()
    sys.exit(app.exec_())
