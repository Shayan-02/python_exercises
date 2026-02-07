import tkinter as tk
from tkinter import ttk
from random import choice


# Game Logic
def get_winner(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = choice(choices)
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Scissors" and computer_choice == "Paper")
        or (player_choice == "Paper" and computer_choice == "Rock")
    ):
        result = f"You Win! Computer chose {computer_choice}"
    else:
        result = f"You Lose! Computer chose {computer_choice}"
    result_label.config(text=result)


# Setting up the GUI
root = tk.Tk()
root.title("Rock Paper Scissors")

# Label
tk.Label(root, text="Choose your option:").pack()

# Combobox for player to choose Rock, Paper, or Scissors
player_choice = ttk.Combobox(root, values=["Rock", "Paper", "Scissors"])
player_choice.current(0)  # Set default option
player_choice.pack()

# Play Button
play_button = tk.Button(
    root, text="Play", command=lambda: get_winner(player_choice.get())
)
play_button.pack()

# Label to display result
result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

# Start the main loop
root.mainloop()
