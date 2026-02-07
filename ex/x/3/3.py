import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

# اتصال به دیتابیس
conn = sqlite3.connect("library.db")
c = conn.cursor()

# ساخت جدول کتاب‌ها
c.execute(
    """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    isbn TEXT,
    category TEXT
)
"""
)
conn.commit()


# تابع‌های کمکی
def refresh_books():
    listbox.delete(*listbox.get_children())
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    for book in books:
        listbox.insert("", "end", values=book)


def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    isbn = entry_isbn.get()
    category = entry_category.get()

    if title and author and year:
        c.execute(
            "INSERT INTO books (title, author, year, isbn, category) VALUES (?, ?, ?, ?, ?)",
            (title, author, year, isbn, category),
        )
        conn.commit()
        refresh_books()
        clear_entries()
    else:
        messagebox.showwarning("خطا در ورودی", "عنوان، نویسنده و سال الزامی هستند.")


def update_book():
    selected = listbox.selection()
    if not selected:
        messagebox.showwarning("خطا در انتخاب", "لطفا یک کتاب را انتخاب کنید.")
        return

    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    isbn = entry_isbn.get()
    category = entry_category.get()

    if title and author and year:
        book_id = listbox.item(selected[0])["values"][0]
        c.execute(
            "UPDATE books SET title=?, author=?, year=?, isbn=?, category=? WHERE id=?",
            (title, author, year, isbn, category, book_id),
        )
        conn.commit()
        refresh_books()
        clear_entries()
    else:
        messagebox.showwarning("خطا در ورودی", "عنوان، نویسنده و سال الزامی هستند.")


def delete_book():
    selected = listbox.selection()
    if not selected:
        messagebox.showwarning("خطا در انتخاب", "لطفا یک کتاب را انتخاب کنید.")
        return

    book_id = listbox.item(selected[0])["values"][0]
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    refresh_books()


def search_books():
    query = entry_search.get()
    listbox.delete(*listbox.get_children())

    c.execute(
        "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR category LIKE ?",
        ("%" + query + "%", "%" + query + "%", "%" + query + "%"),
    )
    books = c.fetchall()
    for book in books:
        listbox.insert("", "end", values=book)


def load_book():
    selected = listbox.selection()
    if not selected:
        messagebox.showwarning("خطا در انتخاب", "لطفا یک کتاب را انتخاب کنید.")
        return

    book = listbox.item(selected[0])["values"]
    clear_entries()
    entry_title.insert(END, book[1])
    entry_author.insert(END, book[2])
    entry_year.insert(END, book[3])
    entry_isbn.insert(END, book[4])
    entry_category.insert(END, book[5])


def clear_entries():
    entry_title.delete(0, END)
    entry_author.delete(0, END)
    entry_year.delete(0, END)
    entry_isbn.delete(0, END)
    entry_category.delete(0, END)


# رابط کاربری
root = Tk()
root.title("سیستم مدیریت کتابخانه")

frame = Frame(root)
frame.pack(pady=20)

Label(frame, text="عنوان").grid(row=0, column=0, padx=10, pady=5, sticky=E)
Label(frame, text="نویسنده").grid(row=1, column=0, padx=10, pady=5, sticky=E)
Label(frame, text="سال انتشار").grid(row=2, column=0, padx=10, pady=5, sticky=E)
Label(frame, text="ISBN").grid(row=3, column=0, padx=10, pady=5, sticky=E)
Label(frame, text="دسته‌بندی").grid(row=4, column=0, padx=10, pady=5, sticky=E)

entry_title = Entry(frame, width=30)
entry_title.grid(row=0, column=1, padx=20, pady=5)
entry_author = Entry(frame, width=30)
entry_author.grid(row=1, column=1, padx=20, pady=5)
entry_year = Entry(frame, width=30)
entry_year.grid(row=2, column=1, padx=20, pady=5)
entry_isbn = Entry(frame, width=30)
entry_isbn.grid(row=3, column=1, padx=20, pady=5)
entry_category = Entry(frame, width=30)
entry_category.grid(row=4, column=1, padx=20, pady=5)

button_frame = Frame(root)
button_frame.pack(pady=20)

add_btn = Button(button_frame, text="افزودن کتاب", command=add_book)
add_btn.grid(row=0, column=0, padx=10)

update_btn = Button(button_frame, text="ویرایش کتاب", command=update_book)
update_btn.grid(row=0, column=1, padx=10)

delete_btn = Button(button_frame, text="حذف کتاب", command=delete_book)
delete_btn.grid(row=0, column=2, padx=10)

load_btn = Button(button_frame, text="بارگذاری کتاب", command=load_book)
load_btn.grid(row=0, column=3, padx=10)

search_frame = Frame(root)
search_frame.pack(pady=10)

Label(search_frame, text="جستجو").grid(row=0, column=0, padx=10, pady=5, sticky=E)
entry_search = Entry(search_frame, width=30)
entry_search.grid(row=0, column=1, padx=20, pady=5)
search_btn = Button(search_frame, text="جستجو", command=search_books)
search_btn.grid(row=0, column=2, padx=10)

listbox_frame = Frame(root)
listbox_frame.pack(pady=10)

columns = ("ID", "Title", "Author", "Year", "ISBN", "Category")
listbox = tTreeview(listbox_frame, columns=columns, show="headings")
for col in columns:
    listbox.heading(col, text=col)
    listbox.column(col, width=100)

listbox.pack(fill="both", expand=True)

refresh_books()

root.mainloop()
