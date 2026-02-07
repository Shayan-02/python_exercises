# Import the 'choice' function from the 'random' module and alias it as 'c'
from random import choice as c

# Define possible choices in the game
choices = ["rock", "paper", "scissors"]

# Generate a random choice for the computer
computer_choice = c(choices)

# Initialize scores for the user and computer
user, computer = 0, 0

# Prompt the user to enter their name
user_name = input("enter your name: ")

# Loop through 5 rounds of the game
for i in range(1, 6):
    # Prompt the user to make a choice from the options
    user_choice = input(f"{user_name} enter your choice {i} ({', '.join(choices)}): ")

    # Check if the user's choice is valid
    if user_choice in choices:
        # Check if both choices are the same
        if user_choice == computer_choice:
            print(f"both players selected {user_choice}. it's a tie!")
        elif user_choice == "rock":
            # Determine the outcome if the user chooses "rock"
            if computer_choice == "scissors":
                print(f"rock smashes scissors! {user_name} wins this round")
                user += 1
            else:
                print("paper covers rock! computer wins this round")
                computer += 1
        elif user_choice == "paper":
            # Determine the outcome if the user chooses "paper"
            if computer_choice == "rock":
                print(f"paper covers rock! {user_name} wins this round")
                user += 1
            else:
                print("scissors cuts paper! computer wins this round")
                computer += 1
        else:
            # Determine the outcome if the user chooses "scissors"
            if computer_choice == "paper":
                print(f"scissors cuts paper! {user_name} wins this round")
                user += 1
            else:
                print("rock smashes scissors! computer wins this round")
                computer += 1

# Determine the final result after 5 rounds
if (user + computer) == 5:
    print(f"{user_name} wins {user} times and computer wins {computer} times")
else:
    print(f"{user_name} wins {user} times and computer wins {computer} times and tie {5 - (user + computer)} times")

# End of the game
