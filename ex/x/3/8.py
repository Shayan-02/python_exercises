import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QComboBox,
    QMessageBox,
    QDialog,
    QDialogButtonBox,
    QDateEdit,
    QCheckBox,
    QMainWindow,
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon


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


# Task Detail Dialog Class
class TaskDetailDialog(QDialog):
    def __init__(self, task=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Task Details")
        self.setModal(True)
        self.setLayout(QFormLayout())

        self.title_input = QLineEdit(self)
        self.priority_input = QLineEdit(self)
        self.due_date_input = QDateEdit(self)
        self.due_date_input.setCalendarPopup(True)
        self.due_date_input.setDisplayFormat("yyyy-MM-dd")
        self.status_checkbox = QCheckBox("Completed", self)

        if task:
            self.task_id = task[0]
            self.title_input.setText(task[1])
            self.priority_input.setText(str(task[2]))
            self.due_date_input.setDate(QDate.fromString(task[3], "yyyy-MM-dd"))
            self.status_checkbox.setChecked(task[4] == "Completed")
        else:
            self.task_id = None

        self.layout().addRow(QLabel("Title:"), self.title_input)
        self.layout().addRow(QLabel("Priority (1-5):"), self.priority_input)
        self.layout().addRow(QLabel("Due Date:"), self.due_date_input)
        self.layout().addRow(self.status_checkbox)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout().addWidget(buttons)

    def get_data(self):
        return (
            self.title_input.text(),
            int(self.priority_input.text()),
            self.due_date_input.date().toString("yyyy-MM-dd"),
            "Completed" if self.status_checkbox.isChecked() else "Pending",
        )


# Main To-Do List Application Class
class TodoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.setWindowTitle("Advanced To-Do List App")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Filter and Sort Controls
        control_layout = QHBoxLayout()
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["All", "Pending", "Completed"])
        self.filter_combo.currentIndexChanged.connect(self.refresh_tasks)
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["Priority", "Due Date"])
        self.sort_combo.currentIndexChanged.connect(self.refresh_tasks)

        control_layout.addWidget(QLabel("Filter:"))
        control_layout.addWidget(self.filter_combo)
        control_layout.addWidget(QLabel("Sort By:"))
        control_layout.addWidget(self.sort_combo)

        layout.addLayout(control_layout)

        # Task Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Title", "Priority", "Due Date", "Status"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.doubleClicked.connect(self.edit_task)

        layout.addWidget(self.table)

        # Action Buttons
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add Task")
        add_btn.clicked.connect(self.add_task)
        delete_btn = QPushButton("Delete Task")
        delete_btn.clicked.connect(self.delete_task)
        mark_completed_btn = QPushButton("Mark Completed")
        mark_completed_btn.clicked.connect(self.mark_completed)

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(delete_btn)
        btn_layout.addWidget(mark_completed_btn)

        layout.addLayout(btn_layout)

        self.refresh_tasks()

    def refresh_tasks(self):
        filter_status = (
            None
            if self.filter_combo.currentText() == "All"
            else self.filter_combo.currentText()
        )
        sort_by = (
            "priority" if self.sort_combo.currentText() == "Priority" else "due_date"
        )

        self.table.setRowCount(0)
        tasks = self.db.fetch_tasks(filter_status=filter_status, sort_by=sort_by)
        for task in tasks:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for col, data in enumerate(task):
                self.table.setItem(row_position, col, QTableWidgetItem(str(data)))

    def add_task(self):
        dialog = TaskDetailDialog()
        if dialog.exec_() == QDialog.Accepted:
            title, priority, due_date, status = dialog.get_data()
            self.db.insert_task(title, priority, due_date, status)
            self.refresh_tasks()

    def edit_task(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(
                self, "Selection Error", "Please select a task to edit."
            )
            return

        task_id = int(self.table.item(selected, 0).text())
        task = [item.text() for item in self.table.item(selected, i) for i in range(5)]
        task = (task_id, *task[1:])

        dialog = TaskDetailDialog(task)
        if dialog.exec_() == QDialog.Accepted:
            title, priority, due_date, status = dialog.get_data()
            self.db.update_task(task_id, title, priority, due_date, status)
            self.refresh_tasks()

    def delete_task(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(
                self, "Selection Error", "Please select a task to delete."
            )
            return

        task_id = int(self.table.item(selected, 0).text())
        self.db.delete_task(task_id)
        self.refresh_tasks()

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
        self.refresh_tasks()

    def closeEvent(self, event):
        self.db.close()
        event.accept()


# Main loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))  # Optionally set a custom icon
    window = TodoListApp()
    window.show()
    sys.exit(app.exec_())
