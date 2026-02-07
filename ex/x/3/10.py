import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
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
    QTabWidget,
    QMessageBox,
    QDialog,
    QDialogButtonBox,
    QComboBox,
    QDateEdit,
)
from PyQt5.QtCore import Qt, QDate


# Database Manager Class
class DatabaseManager:
    def __init__(self, db_name="university.db"):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.c.execute(
            """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dob TEXT,
            major TEXT
        )
        """
        )
        self.c.execute(
            """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            name TEXT NOT NULL,
            instructor TEXT
        )
        """
        )
        self.c.execute(
            """
        CREATE TABLE IF NOT EXISTS enrollments (
            student_id INTEGER,
            course_id INTEGER,
            grade TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(course_id) REFERENCES courses(id),
            PRIMARY KEY(student_id, course_id)
        )
        """
        )
        self.conn.commit()

    def insert_student(self, name, dob, major):
        self.c.execute(
            "INSERT INTO students (name, dob, major) VALUES (?, ?, ?)",
            (name, dob, major),
        )
        self.conn.commit()

    def update_student(self, student_id, name, dob, major):
        self.c.execute(
            "UPDATE students SET name=?, dob=?, major=? WHERE id=?",
            (name, dob, major, student_id),
        )
        self.conn.commit()

    def delete_student(self, student_id):
        self.c.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.conn.commit()

    def insert_course(self, code, name, instructor):
        self.c.execute(
            "INSERT INTO courses (code, name, instructor) VALUES (?, ?, ?)",
            (code, name, instructor),
        )
        self.conn.commit()

    def update_course(self, course_id, code, name, instructor):
        self.c.execute(
            "UPDATE courses SET code=?, name=?, instructor=? WHERE id=?",
            (code, name, instructor, course_id),
        )
        self.conn.commit()

    def delete_course(self, course_id):
        self.c.execute("DELETE FROM courses WHERE id=?", (course_id,))
        self.conn.commit()

    def enroll_student(self, student_id, course_id, grade):
        self.c.execute(
            "INSERT OR REPLACE INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)",
            (student_id, course_id, grade),
        )
        self.conn.commit()

    def fetch_students(self):
        self.c.execute("SELECT * FROM students")
        return self.c.fetchall()

    def fetch_courses(self):
        self.c.execute("SELECT * FROM courses")
        return self.c.fetchall()

    def fetch_enrollments(self):
        self.c.execute(
            """
        SELECT students.name, courses.name, enrollments.grade
        FROM enrollments
        JOIN students ON enrollments.student_id = students.id
        JOIN courses ON enrollments.course_id = courses.id
        """
        )
        return self.c.fetchall()

    def close(self):
        self.conn.close()


# Student Detail Dialog
class StudentDetailDialog(QDialog):
    def __init__(self, student=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Student Details")
        self.setModal(True)
        self.setLayout(QFormLayout())

        self.name_input = QLineEdit(self)
        self.dob_input = QDateEdit(self)
        self.dob_input.setCalendarPopup(True)
        self.dob_input.setDisplayFormat("yyyy-MM-dd")
        self.major_input = QLineEdit(self)

        if student:
            self.student_id = student[0]
            self.name_input.setText(student[1])
            self.dob_input.setDate(QDate.fromString(student[2], "yyyy-MM-dd"))
            self.major_input.setText(student[3])
        else:
            self.student_id = None

        self.layout().addRow(QLabel("Name:"), self.name_input)
        self.layout().addRow(QLabel("Date of Birth:"), self.dob_input)
        self.layout().addRow(QLabel("Major:"), self.major_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout().addWidget(buttons)

    def get_data(self):
        return (
            self.name_input.text(),
            self.dob_input.date().toString("yyyy-MM-dd"),
            self.major_input.text(),
        )


# Course Detail Dialog
class CourseDetailDialog(QDialog):
    def __init__(self, course=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Course Details")
        self.setModal(True)
        self.setLayout(QFormLayout())

        self.code_input = QLineEdit(self)
        self.name_input = QLineEdit(self)
        self.instructor_input = QLineEdit(self)

        if course:
            self.course_id = course[0]
            self.code_input.setText(course[1])
            self.name_input.setText(course[2])
            self.instructor_input.setText(course[3])
        else:
            self.course_id = None

        self.layout().addRow(QLabel("Code:"), self.code_input)
        self.layout().addRow(QLabel("Name:"), self.name_input)
        self.layout().addRow(QLabel("Instructor:"), self.instructor_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout().addWidget(buttons)

    def get_data(self):
        return (
            self.code_input.text(),
            self.name_input.text(),
            self.instructor_input.text(),
        )


# Main University Management App
class UniversityApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.setWindowTitle("University Management System")
        self.setGeometry(100, 100, 900, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_students_tab(), "Students")
        self.tabs.addTab(self.create_courses_tab(), "Courses")
        self.tabs.addTab(self.create_enrollments_tab(), "Enrollments")

        layout.addWidget(self.tabs)

    def create_students_tab(self):
        students_tab = QWidget()
        layout = QVBoxLayout(students_tab)

        self.students_table = QTableWidget()
        self.students_table.setColumnCount(4)
        self.students_table.setHorizontalHeaderLabels(
            ["ID", "Name", "Date of Birth", "Major"]
        )
        self.students_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.students_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.students_table.doubleClicked.connect(self.edit_student)

        layout.addWidget(self.students_table)

        button_layout = QHBoxLayout()
        add_student_btn = QPushButton("Add Student")
        add_student_btn.clicked.connect(self.add_student)
        delete_student_btn = QPushButton("Delete Student")
        delete_student_btn.clicked.connect(self.delete_student)

        button_layout.addWidget(add_student_btn)
        button_layout.addWidget(delete_student_btn)
        layout.addLayout(button_layout)

        self.refresh_students()

        return students_tab

    def create_courses_tab(self):
        courses_tab = QWidget()
        layout = QVBoxLayout(courses_tab)

        self.courses_table = QTableWidget()
        self.courses_table.setColumnCount(4)
        self.courses_table.setHorizontalHeaderLabels(
            ["ID", "Code", "Name", "Instructor"]
        )
        self.courses_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.courses_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.courses_table.doubleClicked.connect(self.edit_course)

        layout.addWidget(self.courses_table)

        button_layout = QHBoxLayout()
        add_course_btn = QPushButton("Add Course")
        add_course_btn.clicked.connect(self.add_course)
        delete_course_btn = QPushButton("Delete Course")
        delete_course_btn.clicked.connect(self.delete_course)

        button_layout.addWidget(add_course_btn)
        button_layout.addWidget(delete_course_btn)
        layout.addLayout(button_layout)

        self.refresh_courses()

        return courses_tab

    def create_enrollments_tab(self):
        enrollments_tab = QWidget()
        layout = QVBoxLayout(enrollments_tab)

        self.enrollments_table = QTableWidget()
        self.enrollments_table.setColumnCount(3)
        self.enrollments_table.setHorizontalHeaderLabels(["Student", "Course", "Grade"])
        self.enrollments_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.enrollments_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.enrollments_table.doubleClicked.connect(self.edit_enrollment)

        layout.addWidget(self.enrollments_table)

        button_layout = QHBoxLayout()
        add_enrollment_btn = QPushButton("Add Enrollment")
        add_enrollment_btn.clicked.connect(self.add_enrollment)

        button_layout.addWidget(add_enrollment_btn)
        layout.addLayout(button_layout)

        self.refresh_enrollments()

        return enrollments_tab

    def refresh_students(self):
        self.students_table.setRowCount(0)
        students = self.db.fetch_students()
        for student in students:
            row = self.students_table.rowCount()
            self.students_table.insertRow(row)
            for col, value in enumerate(student):
                self.students_table.setItem(row, col, QTableWidgetItem(str(value)))

    def refresh_courses(self):
        self.courses_table.setRowCount(0)
        courses = self.db.fetch_courses()
        for course in courses:
            row = self.courses_table.rowCount()
            self.courses_table.insertRow(row)
            for col, value in enumerate(course):
                self.courses_table.setItem(row, col, QTableWidgetItem(str(value)))

    def refresh_enrollments(self):
        self.enrollments_table.setRowCount(0)
        enrollments = self.db.fetch_enrollments()
        for enrollment in enrollments:
            row = self.enrollments_table.rowCount()
            self.enrollments_table.insertRow(row)
            for col, value in enumerate(enrollment):
                self.enrollments_table.setItem(row, col, QTableWidgetItem(str(value)))

    def add_student(self):
        dialog = StudentDetailDialog(parent=self)
        if dialog.exec_() == QDialog.Accepted:
            name, dob, major = dialog.get_data()
            self.db.insert_student(name, dob, major)
            self.refresh_students()

    def edit_student(self, index):
        selected_row = self.students_table.currentRow()
        student_id = int(self.students_table.item(selected_row, 0).text())
        student = [
            self.students_table.item(selected_row, i).text() for i in range(1, 4)
        ]
        dialog = StudentDetailDialog(student=([student_id] + student), parent=self)
        if dialog.exec_() == QDialog.Accepted:
            name, dob, major = dialog.get_data()
            self.db.update_student(student_id, name, dob, major)
            self.refresh_students()

    def delete_student(self):
        selected_row = self.students_table.currentRow()
        if selected_row >= 0:
            student_id = int(self.students_table.item(selected_row, 0).text())
            self.db.delete_student(student_id)
            self.refresh_students()
        else:
            QMessageBox.warning(
                self, "No Selection", "Please select a student to delete."
            )

    def add_course(self):
        dialog = CourseDetailDialog(parent=self)
        if dialog.exec_() == QDialog.Accepted:
            code, name, instructor = dialog.get_data()
            self.db.insert_course(code, name, instructor)
            self.refresh_courses()

    def edit_course(self, index):
        selected_row = self.courses_table.currentRow()
        course_id = int(self.courses_table.item(selected_row, 0).text())
        course = [self.courses_table.item(selected_row, i).text() for i in range(1, 4)]
        dialog = CourseDetailDialog(course=([course_id] + course), parent=self)
        if dialog.exec_() == QDialog.Accepted:
            code, name, instructor = dialog.get_data()
            self.db.update_course(course_id, code, name, instructor)
            self.refresh_courses()

    def delete_course(self):
        selected_row = self.courses_table.currentRow()
        if selected_row >= 0:
            course_id = int(self.courses_table.item(selected_row, 0).text())
            self.db.delete_course(course_id)
            self.refresh_courses()
        else:
            QMessageBox.warning(
                self, "No Selection", "Please select a course to delete."
            )

    def add_enrollment(self):
        enroll_dialog = EnrollmentDialog(self.db, self, parent=self)
        if enroll_dialog.exec_() == QDialog.Accepted:
            student_id = enroll_dialog.student_combo.currentData()
            course_id = enroll_dialog.course_combo.currentData()
            grade = enroll_dialog.grade_input.text()
            self.db.enroll_student(student_id, course_id, grade)
            self.refresh_enrollments()

    def edit_enrollment(self, index):
        pass  # Editing enrollment is omitted for simplicity


class EnrollmentDialog(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.setWindowTitle("Enroll Student")
        self.setModal(True)
        self.setLayout(QFormLayout())

        self.student_combo = QComboBox(self)
        self.course_combo = QComboBox(self)
        self.grade_input = QLineEdit(self)

        students = self.db.fetch_students()
        for student in students:
            self.student_combo.addItem(student[1], student[0])

        courses = self.db.fetch_courses()
        for course in courses:
            self.course_combo.addItem(course[2], course[0])

        self.layout().addRow(QLabel("Student:"), self.student_combo)
        self.layout().addRow(QLabel("Course:"), self.course_combo)
        self.layout().addRow(QLabel("Grade:"), self.grade_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout().addWidget(buttons)

    def get_data(self):
        return (
            self.student_combo.currentData(),
            self.course_combo.currentData(),
            self.grade_input.text(),
        )


# Main loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UniversityApp()
    window.show()
    sys.exit(app.exec_())
