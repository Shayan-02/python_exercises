# https://quera.org/problemset/3537

def soal_zard(num:int) -> str:
    """
    This function takes an integer input and returns a string with the input repeated.

    Args:
        num (int): An integer representing the number of times you want to repeat a certain action or
        sequence

    Returns:
        str: w + o * n + w!
    """
    return f"w{num*"o"}w!" if num > 0 else "invalid input" 


print(soal_zard(int(input())))