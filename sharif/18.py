import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    text_area.delete(1.0, END)


def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if file_path:
        text_area.delete(1.0, END)
        with open(file_path, "r") as file:
            text_area.insert(END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, END))


def exit_app():
    root.quit()


# Initialize the main window
root = Tk()
root.title("Notepad")
root.geometry("600x400")

# Create a Text widget for the notepad area
text_area = Text(root, wrap="word", undo=True)
text_area.pack(expand=True, fill="both")

# Create a Menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Run the application
root.mainloop()
