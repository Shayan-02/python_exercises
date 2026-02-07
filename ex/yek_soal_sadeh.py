def repeat(n:int) -> str:
    """
    This function takes an integer input and returns a string with the input repeated.
    
    :param n: An integer representing the number of times you want to repeat a certain action or
    sequence
    :type n: int

    Returns:
        str: man khoshghlab hastam * n
    """
    return "\n".join(["man khoshghlab hastam" for _ in range(n)])


print(repeat(int(input())))
