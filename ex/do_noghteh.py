def do_noghteh(x1: int, y1: int, x2: int, y2: int) -> str:
    """
    Determine if two points are on the same line or not.

    Args:
        x1 (int): The x-coordinate of the first point.
        y1 (int): The y-coordinate of the first point.
        x2 (int): The x-coordinate of the second point.
        y2 (int): The y-coordinate of the second point.

    Returns:
        str: "Vertical" if the two points are on the same vertical line,
             "Horizontal" if the two points are on the same horizontal line,
             "Try again" otherwise.
    """
    # Check if the points are on the same vertical line
    if x1 == x2:
        return "Vertical"
    # Check if the points are on the same horizontal line
    elif y1 == y2:
        return "Horizontal"
    # If the points are not on the same line
    else:
        return "Try again"



x1, y1, x2, y2 = input().split()
print(do_noghteh(x1, y1, x2, y2))