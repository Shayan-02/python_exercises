import sqlite3
from tkinter import *
from tkinter import messagebox

# Database setup
conn = sqlite3.connect("bookstore.db")
c = conn.cursor()

c.execute(
    """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    isbn TEXT
)
"""
)
conn.commit()


# Functions for GUI
def refresh_books():
    listbox.delete(0, END)
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    for book in books:
        listbox.insert(
            END, f"{book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]}"
        )


def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    isbn = entry_isbn.get()

    if title and author:
        c.execute(
            "INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)",
            (title, author, year, isbn),
        )
        conn.commit()
        refresh_books()
        entry_title.delete(0, END)
        entry_author.delete(0, END)
        entry_year.delete(0, END)
        entry_isbn.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Title and Author are required fields.")


def update_book():
    selected_book = listbox.curselection()
    if not selected_book:
        messagebox.showwarning("Selection Error", "Please select a book to update.")
        return

    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    isbn = entry_isbn.get()

    if title and author:
        book_id = listbox.get(selected_book).split(" | ")[0]
        c.execute(
            "UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",
            (title, author, year, isbn, book_id),
        )
        conn.commit()
        refresh_books()
    else:
        messagebox.showwarning("Input Error", "Title and Author are required fields.")


def delete_book():
    selected_book = listbox.curselection()
    if not selected_book:
        messagebox.showwarning("Selection Error", "Please select a book to delete.")
        return

    book_id = listbox.get(selected_book).split(" | ")[0]
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    refresh_books()


def load_book():
    selected_book = listbox.curselection()
    if not selected_book:
        messagebox.showwarning("Selection Error", "Please select a book to load.")
        return

    book = listbox.get(selected_book).split(" | ")
    entry_title.delete(0, END)
    entry_title.insert(END, book[1])
    entry_author.delete(0, END)
    entry_author.insert(END, book[2])
    entry_year.delete(0, END)
    entry_year.insert(END, book[3])
    entry_isbn.delete(0, END)
    entry_isbn.insert(END, book[4])


# GUI Layout
root = Tk()
root.title("Bookstore App")

frame = Frame(root)
frame.pack(pady=20)

Label(frame, text="Title").grid(row=0, column=0)
Label(frame, text="Author").grid(row=1, column=0)
Label(frame, text="Year").grid(row=2, column=0)
Label(frame, text="ISBN").grid(row=3, column=0)

entry_title = Entry(frame, width=30)
entry_title.grid(row=0, column=1, padx=20)
entry_author = Entry(frame, width=30)
entry_author.grid(row=1, column=1, padx=20)
entry_year = Entry(frame, width=30)
entry_year.grid(row=2, column=1, padx=20)
entry_isbn = Entry(frame, width=30)
entry_isbn.grid(row=3, column=1, padx=20)

add_btn = Button(frame, text="Add Book", command=add_book)
add_btn.grid(row=4, column=0, pady=10)

update_btn = Button(frame, text="Update Book", command=update_book)
update_btn.grid(row=4, column=1, pady=10)

delete_btn = Button(frame, text="Delete Book", command=delete_book)
delete_btn.grid(row=5, column=0, pady=10)

load_btn = Button(frame, text="Load Book", command=load_book)
load_btn.grid(row=5, column=1, pady=10)

listbox = Listbox(root, width=70, height=15)
listbox.pack(pady=20)

refresh_books()

root.mainloop()
