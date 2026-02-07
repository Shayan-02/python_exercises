def sum_of_digits(x: int) -> int:
    """
    Returns the sum of the digits of a given number.
    
    Parameters:
    x (int): The number to sum the digits of.
    
    Returns:
    int: The sum of the digits of x.
    """
    return sum(int(d) for d in str(x))


def sum_of_prime_factors(x: int) -> int:
    """
    Returns the sum of the prime factors of a given number.
    
    Parameters:
    x (int): The number to sum the prime factors of.
    
    Returns:
    int: The sum of the prime factors of x.
    """
    # Initialize the sum of the prime factors
    sum_of_prime_factors = 0
    
    # Iterate through all numbers from 2 to x
    for i in range(2, x + 1):
        # Check if the number is a prime factor of x
        if x % i == 0 and is_prime(i):
            # Add the prime factor to the sum
            sum_of_prime_factors += i
    
    # Return the sum of the prime factors
    return sum_of_prime_factors


def is_prime(n: int) -> bool:
    """
    Checks if a given number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # Check if n is less than 2
    if n < 2:
        # Return False if n is less than 2
        return False
    
    # Iterate through all numbers from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        # Check if n is divisible by the number
        if n % i == 0:
            # Return False if n is divisible by the number
            return False
    
    # Return True if n is not divisible by any of the numbers
    return True


def find_father(t: int, numbers: list[int]) -> list[str]:
    """
    Finds the father number for a given list of numbers.
    
    Parameters:
    t (int): The number of elements in the list.
    numbers (list): A list of integers.
    
    Returns:
    list: A list of strings, where each string is either "Yes" or "No" and indicates
    whether the father number was found for the corresponding element in the input list.
    """
    results = []
    for n in numbers:
        found = False
        # Iterate through all numbers from max(1, n - 100) to n
        for x in range(max(1, n - 100), n):
            # Check if the condition is satisfied
            if x + sum_of_digits(x) + sum_of_prime_factors(x) == n:
                found = True
                break
        # Add the result to the list
        results.append("Yes" if found else "No")
    return results



# Input
t = int(input())
numbers = [int(input()) for _ in range(t)]

# Output
results = find_father(t, numbers)
for result in results:
    print(result)
