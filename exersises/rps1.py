from tkinter import *
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
root = Tk()
root.title("Rock Paper Scissors")

# Variable to store the player's choice
player_choice = StringVar()
player_choice.set("Rock")  # Default selection

# Radio buttons for player to choose Rock, Paper, or Scissors
Label(root, text="Choose your option:").pack(anchor=W)
Radiobutton(root, text="Rock", variable=player_choice, value="Rock").pack(anchor=W)
Radiobutton(root, text="Paper", variable=player_choice, value="Paper").pack(anchor=W)
Radiobutton(root, text="Scissors", variable=player_choice, value="Scissors").pack(
    anchor=W
)

# Button to play the game
play_button = Button(root, text="Play", command=lambda: get_winner(player_choice.get()))
play_button.pack()

# Label to display the result
result_label = Label(root, text="", fg="blue")
result_label.pack()

# Start the main loop
root.mainloop()
