def print_squares(a, b):
    # Check if a and b are in the correct order
    if a < b:
        print("Wrong order!")
        return

    # Calculate the areas
    area_a = a * a
    area_b = b * b

    # Check if the difference is even
    if (area_a - area_b) % 2 != 0:
        print("Wrong difference!")
        return

    # Print the larger square
    for i in range(a):
        if i < b or i >= a - b:
            print("* " * a)
        else:
            print("* " * b + "  " * (a - 2 * b) + "* " * b)
    print()


# Example usage
a = 7
b = 3
print_squares(a, b)
