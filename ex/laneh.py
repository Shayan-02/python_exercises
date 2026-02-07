def laneh(n: int, m: int) -> str:
    """
    This function determines if we can reach the m-th house from the n-th house.

    Args:
        n (int): The number of the house we are currently in.
        m (int): The number of the house we want to reach.

    Returns:
        str: "Yes" if we can reach the m-th house from the n-th house, "No" otherwise.
    """
    # If we are already in the m-th house or any house after that, we can reach it
    if n >= m:
        return "Yes"
    else:
        # Otherwise, we can not reach the m-th house
        return "No"


n, m = map(int, input().split())

print(laneh(n, m))
