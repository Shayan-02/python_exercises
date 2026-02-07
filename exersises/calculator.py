from tkinter import *


# Function to handle button clicks
def button_click(value):
    current_text = entry.get()
    entry.delete(0, END)
    entry.insert(0, current_text + str(value))


# Function to clear the entry widget
def clear():
    entry.delete(0, END)


# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")


# Set up the main window
root = Tk()
root.title("Calculator")
root.resizable(0, 0)

# Entry widget to display expressions
entry = Entry(root, font=("Arial", 24, "bold"), borderwidth=5, relief=RIDGE, justify="left")
entry.grid(row=0, column=0, columnspan=4, padx=0, pady=0, sticky="nsew")

# Button configurations
button_config = {"padx": 20, "pady": 20, "bd": 1, "fg": "white", "font": ("Arial", 18, "bold")}

# Number buttons
numbers = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("0", 4, 1),
]

for text, row, col in numbers:
    Button(
        root,
        text=text,
        bg="black",
        command=lambda t=text: button_click(t),
        **button_config
    ).grid(row=row, column=col, sticky="nsew")

# Operation buttons
operations = [
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 3),
    ("C", 4, 0),
    ("=", 4, 2),
]

for text, row, col in operations:
    color = "orange" if text in ("+", "-", "*", "/") else "gray"
    Button(
        root,
        text=text,
        bg=color,
        command=lambda t=text: button_click(t) if t != "=" else evaluate(),
        **button_config
    ).grid(row=row, column=col, sticky="nsew")

# Special functions
Button(root, text="C", bg="orange", command=clear, **button_config).grid(row=4, column=0, sticky="nsew")
Button(root, text="=", bg="orange", command=evaluate, **button_config).grid(row=4, column=2, sticky="nsew")

root.mainloop()