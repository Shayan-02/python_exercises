def separator(ls: list[int]) -> tuple[list[int], list[int]]:
    """
    Separates the list of numbers into two lists - one containing even numbers and the other containing odd numbers.
    :param ls: A list of integers
    :return: A tuple of two lists - one containing even numbers and the other containing odd numbers
    """
    # Initialize empty lists
    odd = []
    even = []

    # Iterate through the list
    for _ in ls:
        # Check if the number is even or odd
        if _ % 2 == 0:
            # If even, append it to the even list
            even.append(_)
        else:
            # If odd, append it to the odd list
            odd.append(_)

    # Return the two lists
    return even, odd

x = input().split()
x = list(map(int, x))
print(separator(x))
