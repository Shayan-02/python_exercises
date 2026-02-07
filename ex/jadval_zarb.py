def jadval_zarb(n: int) -> None:
    """
    Prints the multiplication table for numbers 1 to n.

    Args:
        n (int): The number of rows and columns in the table.
    """
    # Iterate over the rows
    for i in range(1, n + 1):
        # Iterate over the columns
        for j in range(1, n + 1):
            # Print the product of the current row and column
            print(i * j, end=" ")
        # Print a newline after each row
        print()


jadval_zarb(int(input()))