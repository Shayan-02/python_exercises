def cinama(num1: int, num2: int) -> int:
    """
    This function takes two numbers as input and returns the minimum of the two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The minimum of num1 and num2.
    """
    # Return the minimum of the two numbers
    return min(num1, num2)


num1, num2 = map(int, input().split())
print(cinama(num1, num2))
