def jadeh(n: int)-> int:
    """
    Calculates the maximum number of roads in a city.

    This function takes an integer n as an argument and returns the maximum
    number of roads in a city. The function uses a for loop to iterate through
    all possible combinations of roads and calculates the number of roads in
    each combination. The maximum number of roads is stored in the max_roads
    variable and returned at the end of the function.

    Parameters
    ----------
    n : int
        The number of roads in the city.

    Returns
    -------
    int
        The maximum number of roads in the city.
    """
    max_roads = 0
    # Iterate through all possible combinations of roads
    for i in range(n + 1):
        x = n - i
        roads = (i + 1) * (x + 1)
        # Check if the number of roads in the current combination is higher
        # than the maximum number of roads so far
        if roads > max_roads:
            max_roads = roads
    # Return the maximum number of roads
    return max_roads


n = int(input())

print(jadeh(n))
