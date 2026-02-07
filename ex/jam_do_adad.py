def sum_number(a: int, b: int) -> int:
    """
    This function takes two integers and returns their sum.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b


a, b = map(int, input().split())
print(sum_number(a, b))