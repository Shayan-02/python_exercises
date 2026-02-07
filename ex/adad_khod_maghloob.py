# https://quera.org/problemset/617

def maghloob(num: int) -> str:
    """
    Checks if a given number is a palindrome.

    Args:
        num (int): The number to check.

    Returns:
        str: "YES" if the number is a palindrome, "NO" otherwise.
    """
    return "YES" if str(num) == str(num)[::-1] else "NO"


print(maghloob(int(input())))