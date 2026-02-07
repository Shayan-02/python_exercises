def charging_time(k: int) -> int:
    """
    Calculates the total time required to charge all devices up to the k-th device.

    The time required to charge the i-th device is i. The total time required to
    charge all devices up to the k-th device is the sum of the first k natural numbers,
    which is given by the formula: (k * (k + 1)) // 2.

    Args:
        k (int): The number of the last device to be charged.

    Returns:
        int: The total time required to charge all devices up to the k-th device.
    """
    # Using the sum formula for the first k numbers
    total_time = (k * (k + 1)) // 2
    return total_time


print(charging_time(int(input())))