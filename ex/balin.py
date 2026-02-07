# https://quera.org/problemset/175884

def calculate_floor(string: str) -> int:
    """
    Calculate the final floor of an elevator given a string of commands.

    The string should contain only the characters "U" and "D" which stand for
    "up" and "down" respectively.

    Args:
        string (str): The string of commands.

    Returns:
        int: The final floor of the elevator.
    """
    f = 0
    for i in string:
        if i.lower() == "u":
            # Move the elevator up
            f += 1
        elif i.lower() == "d":
            # Move the elevator down
            f -= 1
        else:
            # If the command is invalid
            print("invalid input")
    return f


print(calculate_floor(input()))