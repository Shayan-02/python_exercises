def game(num: int) -> int:
    """

    This function calculates the difference between the largest and smallest digits in the number.
    Args:
        num (int): a number

    Returns:
        int: difference between the largest and smallest digits in the number.
    """
    a = set(str(num))
    return int(max(a)) - int(min(a))


game(int(input()))