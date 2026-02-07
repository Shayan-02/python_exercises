def barnameh(n: int, l: int, r: int) -> int:
    """
    Calculates the number of days it takes to download a file of size n
    with a download rate of l bytes per day and a maximum download size of r bytes.

    Args:
        n (int): The size of the file in bytes.
        l (int): The download rate in bytes per day.
        r (int): The maximum download size in bytes.

    Returns:
        int: The number of days it takes to download the file.
    """
    day = n // r
    if n % r != 0:
        day += 1
    if day * l > n:
        return -1
    return day


n = int(input())
l, r = map(int, input().split())
print(barnameh(n, l, r))
