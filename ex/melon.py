def can_divide_fruit(h, k):
    """
    Determines if it's possible to divide `h` fruits of one type and `k` fruits of another type
    into two groups such that each group has an integer number of each type of fruit.

    Args:
        h (int): The number of fruits of the first type.
        k (int): The number of fruits of the second type.

    Returns:
        str: "YES" if the fruits can be divided into two groups satisfying the conditions, 
             otherwise "NO".
    """
    # Check if (h + k / 2) is an integer
    if (h + k / 2) % 2 != 0:
        return "NO"
    
    # Compute target value and x, y
    target = h + k / 2
    x = (target - k) / 2
    y = target - 2 * x
    
    # Check if x and y are valid
    if 0 <= x <= h and 0 <= y <= k:
        return "YES"
    else:
        return "NO"

# Read input and convert to integers
h = int(input())
k = int(input())

# Print result
print(can_divide_fruit(h, k))
