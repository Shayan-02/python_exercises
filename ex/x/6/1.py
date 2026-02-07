from tkinter import *
from tkinter import messagebox
import random


# Function to determine the winner
def determine_winner(player_choice):
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

# Variable to store the player's choice
player_choice = StringVar()
player_choice.set("Rock")  # Default selection

# Label
Label(root, text="Choose your move:").pack()

# Radio buttons for player's choice
choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    Radiobutton(root, text=choice, variable=player_choice, value=choice).pack()

Button(
    root, text="Play", command=lambda: determine_winner(player_choice.get())
).pack()

root.mainloop()
