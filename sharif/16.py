def print_square(n):
    """Prints a multiplication square of size n."""

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:2}", end=" ")
        print()


n = int(input())
print_square(n)
