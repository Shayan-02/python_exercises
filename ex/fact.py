def fact(n: int) -> int:
    """
    This function calculates the factorial of a given number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of n.
    """
    # Initialize the factorial to 1
    fact = 1
    # Loop through all numbers from 1 to n, and multiply the current number to the factorial
    for j in range(1, n + 1):
        fact *= j
    # Return the calculated factorial
    return fact

n = int(input())
print(fact(n))