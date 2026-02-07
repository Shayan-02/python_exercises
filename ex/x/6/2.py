import tkinter as tk
from tkinter import ttk, messagebox
import random


# Function to determine the winner
def determine_winner():
    player_choice = combo_box.get()
    if player_choice == "":
        messagebox.showwarning("Warning", "Please choose your move!")
        return

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = f"You win! Computer chose {computer_choice}."
    else:
        result = f"You lose! Computer chose {computer_choice}."

    messagebox.showinfo("Result", result)


# Creating the main window
root = Tk()
root.title("Rock, Paper, Scissors")

# Label
Label(root, text="Choose your move:").pack(pady=10)

# Combobox for player's choice
choices = ["Rock", "Paper", "Scissors"]
combo_box = tCombobox(root, values=choices, state="readonly")
combo_box.pack(pady=5)

# Play button
Button(root, text="Play", command=determine_winner).pack(pady=10)

# Start the GUI loop
root.mainloop()
