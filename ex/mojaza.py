def separator(ls: list) -> tuple:
    """
    The function `separator` takes a list of numbers as input and separates them into two lists - one
    containing even numbers and the other containing odd numbers.
    
    :param ls (list): The `separator` function takes a list of integers as input and separates the numbers into
    two lists - one containing even numbers and the other containing odd numbers
    :return: The `separator` function returns two lists: one containing all the even numbers from the
    input list `ls`, and the other containing all the odd numbers from the input list `ls`.
    """
    odd, even = [], []; [even.append(_) if _ % 2 == 0 else odd.append(_) for _ in ls]; return even, odd


print(separator(list(map(int, input().split()))))
