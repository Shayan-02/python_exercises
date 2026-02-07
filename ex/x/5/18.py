from tkinter import *
import sqlite3

import backend

# function
def exit():
    root.destroy()


def add_item():
    task = entry.get(), entry2.get(), entry3.get(), entry4.get()
    listbox.insert(END, task)


def delete():
    listbox.delete(0, END)
    entry.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)


def search():
    listbox.delete(0, END)
    for row in backend.search(label1.get(), label2.get(), label3.get(), label4.get()):
        listbox.insert(END, row)


def get_selected_row():
    global selected_Tupel
    index = listbox.curselection([1])
    selected_Tupel = listbox.get(index)


def update():
    backend.update(
        selected_Tupel[0], label1.get(), label2.get(), label3.get(), label4.get()
    )


# opening a windose
root = Tk()
root.title("Book Shop")
root.geometry("700x400")

# creating labels
label1 = Label(root, text="item", font=("Arial", 15, "bold"))
label1.place(x=20, y=20)

label2 = Label(root, text="buy", font=("Arial", 15, "bold"))
label2.place(x=420, y=20)

label3 = Label(root, text="sell", font=("Arial", 15, "bold"))
label3.place(x=20, y=100)

label4 = Label(root, text="number", font=("Arial", 15, "bold"))
label4.place(x=420, y=100)

# creating entrys
entry = Entry(root, width=20, bd=2)
entry.place(x=100, y=25)

entry2 = Entry(root, width=20, bd=2)
entry2.place(x=550, y=25)

entry3 = Entry(root, width=20, bd=2)
entry3.place(x=140, y=105)

entry4 = Entry(root, width=20, bd=2)
entry4.place(x=570, y=105)

# listbox
listbox = Listbox(root, width=60)
listbox.place(x=20, y=200)

# button
btn = Button(root, text="add item", width=15, bg="black", fg="white", command=add_item)
btn.place(x=600, y=280)

btn2 = Button(root, text="delete item", bg="black", fg="white", command=delete)
btn2.place(x=630, y=340)

btn3 = Button(root, text="edit item", bg="black", fg="white", command=update)
btn3.place(x=640, y=310)

btn4 = Button(root, text="exit app", bg="black", fg="white", command=exit)
btn4.place(x=645, y=370)

btn5 = Button(root, text="search item", bg="black", fg="white", command=search)
btn5.place(x=565, y=370)

# scrollbar
sc = Scrollbar(root)
sc.place(x=450, y=250)
root.mainloop()
