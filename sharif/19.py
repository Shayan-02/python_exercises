import tkinter as tk
from tkinter import colorchooser


def set_color(new_color):
    global pen_color
    pen_color = new_color


def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        set_color(color)


def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(
        x1, y1, x2, y2, fill=pen_color, outline=pen_color, width=pen_size
    )


def clear_canvas():
    canvas.delete("all")


def draw_shape(shape):
    global current_shape
    current_shape = shape


def on_click(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y


def on_release(event):
    x, y = event.x, event.y
    if current_shape == "rectangle":
        canvas.create_rectangle(
            start_x, start_y, x, y, outline=pen_color, width=pen_size
        )
    elif current_shape == "circle":
        canvas.create_oval(start_x, start_y, x, y, outline=pen_color, width=pen_size)


root = Tk()
root.title("Advanced Tkinter Paint")

pen_color = "black"
pen_size = 3
current_shape = None

# Create canvas
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack(expand=YES, fill=BOTH)

# Bind events for drawing
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonPress-3>", on_click)
canvas.bind("<ButtonRelease-3>", on_release)

# Create buttons for functionalities
color_button = Button(root, text="Choose Color", command=choose_color)
color_button.pack(side=LEFT)

clear_button = Button(root, text="Clear", command=clear_canvas)
clear_button.pack(side=LEFT)

rectangle_button = Button(
    root, text="Rectangle", command=lambda: draw_shape("rectangle")
)
rectangle_button.pack(side=LEFT)

circle_button = Button(root, text="Circle", command=lambda: draw_shape("circle"))
circle_button.pack(side=LEFT)

root.mainloop()
