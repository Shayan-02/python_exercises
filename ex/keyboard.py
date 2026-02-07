def election_name(n: int, keys: list) -> str:
    """
    Simulate a user typing a string with a keyboard with a caps lock key.

    Parameters:
        n (int): The number of keys to press.
        keys (list): A list of strings representing the keys to press. Each string is
            either the name of a key (e.g. "a", "b", etc.) or "CAPS" to toggle the
            caps lock.

    Returns:
        str: The string that results from pressing the given keys with the given
            caps lock state.
    """
    caps_lock = False
    result = []

    # Iterate over the keys to press
    for key in keys:
        if key == "CAPS":
            # Toggle the caps lock state
            caps_lock = not caps_lock
        else:
            # Press the key with the current caps lock state
            if caps_lock:
                result.append(key.upper())
            else:
                result.append(key.lower())

    # Join the characters into a single string and return it
    return "".join(result)


# Input example
n = 10
keys = ["d", "CAPS", "a", "n", "g", "CAPS", "e", "r", "CAPS", "y"]

# Output the result
print(election_name(n, keys))  # Output: dANGerY
