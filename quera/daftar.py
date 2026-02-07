import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main window
root = Tk()
root.title("Rock-Paper-Scissors")

# Colors
bg_color = "#f0f8ff"
button_color = "#8ecae6"
highlight_color = "#ffb703"
label_color = "#023047"

root.configure(bg=bg_color)

# Variables to keep track of scores
user_score = 0
computer_score = 0

# User choice variable
user_choice_var = StringVar(value="Rock")


def play():
    global user_score, computer_score

    user_choice = user_choice_var.get()
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
    messagebox.showinfo("Result", f"Computer chose {computer_choice}.\n{result}")


# Create a label for instructions
instructions = Label(
    root,
    text="Choose Rock, Paper, or Scissors:",
    bg=bg_color,
    fg=label_color,
    font=("Arial", 12),
)
instructions.pack(pady=10)

# Create radio buttons for user to select Rock, Paper, or Scissors
choices_frame = Frame(root, bg=bg_color)
choices_frame.pack()

rock_btn = Radiobutton(
    choices_frame,
    text="Rock",
    variable=user_choice_var,
    value="Rock",
    bg=bg_color,
    fg=label_color,
    selectcolor=highlight_color,
    font=("Arial", 10),
)
rock_btn.pack(anchor=W, padx=20, pady=5)

paper_btn = Radiobutton(
    choices_frame,
    text="Paper",
    variable=user_choice_var,
    value="Paper",
    bg=bg_color,
    fg=label_color,
    selectcolor=highlight_color,
    font=("Arial", 10),
)
paper_btn.pack(anchor=W, padx=20, pady=5)

scissors_btn = Radiobutton(
    choices_frame,
    text="Scissors",
    variable=user_choice_var,
    value="Scissors",
    bg=bg_color,
    fg=label_color,
    selectcolor=highlight_color,
    font=("Arial", 10),
)
scissors_btn.pack(anchor=W, padx=20, pady=5)

# Play button
play_button = Button(
    root,
    text="Play",
    command=play,
    bg=button_color,
    fg="white",
    font=("Arial", 12),
    relief=RAISED,
)
play_button.pack(pady=20)

# Label to display the score
score_label = Label(
    root,
    text="Score - You: 0 | Computer: 0",
    bg=bg_color,
    fg=label_color,
    font=("Arial", 12, "bold"),
)
score_label.pack(pady=10)

# Run the application
root.mainloop()
