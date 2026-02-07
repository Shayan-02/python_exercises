def find_smallest_largest(m: int, s: int)-> None:
    """
    Finds the smallest and largest numbers with m digits and sum s.
    If it's not possible to form such numbers

    Args:
        m (int): The number of digits in the numbers.
        s (int): The sum of the digits in the numbers.

    Returns:
        None
    """
    # If it's not possible to form such numbers
    global smallest, largest
    if s == 0 and m == 1:
        print(0, 0)
        return
    elif s == 0 or s > 9 * m:
        print(-1, -1)
        return
    # Finding largest number
    largest = [0] * m
    remaining = s
    for i in range(m):
        largest[i] = min(9, remaining)
        remaining -= largest[i]
    largest = [str(x) for x in largest]

    # Finding smallest number
    smallest = []
    for i in range(m):
        # Try to find the largest digit that doesn't exceed s
        smallest.append(max(0, min(s - sum(smallest), 9)))
    smallest = [str(x) for x in smallest]

    # Finding largest number
    largest = [0] * m
    remaining = s
    for i in range(m):
        largest[i] = min(9, remaining)
        remaining -= largest[i]
    largest = [str(x) for x in largest]

    # Printing results
    print("".join(smallest[::-1]), "".join(largest))

# Example Usage
# m, s = map(int, input().split())
m, s = 2, 15
find_smallest_largest(m, s)

