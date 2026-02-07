import sqlite3
from tkinter import *
from tkinter import messagebox

# Database setup
conn = sqlite3.connect("contacts.db")
c = conn.cursor()

c.execute(
    """
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT
)
"""
)
conn.commit()

# GUI setup
root = Tk()
root.title("Contact Book")


def refresh_contacts():
    listbox.delete(0, END)
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    for contact in contacts:
        listbox.insert(END, f"{contact[1]} | {contact[2]} | {contact[3]}")


def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name and phone:
        c.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email),
        )
        conn.commit()
        refresh_contacts()
        entry_name.delete(0, END)
        entry_phone.delete(0, END)
        entry_email.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required fields.")


def update_contact():
    selected_contact = listbox.curselection()
    if not selected_contact:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")
        return

    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name and phone:
        contact_id = listbox.get(selected_contact).split(" | ")[0]
        c.execute(
            "UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",
            (name, phone, email, contact_id),
        )
        conn.commit()
        refresh_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required fields.")


def delete_contact():
    selected_contact = listbox.curselection()
    if not selected_contact:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")
        return

    contact_id = listbox.get(selected_contact).split(" | ")[0]
    c.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    refresh_contacts()


def load_contact():
    selected_contact = listbox.curselection()
    if not selected_contact:
        messagebox.showwarning("Selection Error", "Please select a contact to load.")
        return

    contact = listbox.get(selected_contact).split(" | ")
    entry_name.delete(0, END)
    entry_name.insert(END, contact[0])
    entry_phone.delete(0, END)
    entry_phone.insert(END, contact[1])
    entry_email.delete(0, END)
    entry_email.insert(END, contact[2])


# GUI Layout
frame = Frame(root)
frame.pack(pady=20)

Label(frame, text="Name").grid(row=0, column=0)
Label(frame, text="Phone").grid(row=1, column=0)
Label(frame, text="Email").grid(row=2, column=0)

entry_name = Entry(frame, width=30)
entry_name.grid(row=0, column=1, padx=20)
entry_phone = Entry(frame, width=30)
entry_phone.grid(row=1, column=1, padx=20)
entry_email = Entry(frame, width=30)
entry_email.grid(row=2, column=1, padx=20)

add_btn = Button(frame, text="Add Contact", command=add_contact)
add_btn.grid(row=3, column=0, pady=10)

update_btn = Button(frame, text="Update Contact", command=update_contact)
update_btn.grid(row=3, column=1, pady=10)

delete_btn = Button(frame, text="Delete Contact", command=delete_contact)
delete_btn.grid(row=4, column=0, pady=10)

load_btn = Button(frame, text="Load Contact", command=load_contact)
load_btn.grid(row=4, column=1, pady=10)

listbox = Listbox(root, width=50, height=15)
listbox.pack(pady=20)

refresh_contacts()

root.mainloop()
