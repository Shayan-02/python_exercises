def waterMelon(h, k):
    """
    Checks if the fruits can be divided into two groups satisfying the conditions.

    Args:
        h (int): The number of fruits of the first type.
        k (int): The number of fruits of the second type.

    Returns:
        str: "YES" if the fruits can be divided into two groups satisfying the conditions,
             otherwise "NO".
    """
    if ((2 * h) + k) % 2 == 0:
        return "Yes"
    else:
        return "No"


# Print result
print(waterMelon(int(input()), int(input())))
