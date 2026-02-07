
def class_code(n: int) -> int:
    """
    This function takes an integer n as an argument and returns the nth digit of the
    string of numbers from 1 to 4000 concatenated together.

    Parameters:
    n (int): The digit to be returned.

    Returns:
    int: The nth digit of the string of numbers from 1 to 4000 concatenated together.
    """
    a = "".join(map(str, range(1, 4001)))
    return int(a[n - 1])

print(class_code(int(input())))