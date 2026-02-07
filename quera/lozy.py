def print_diamonds(n):
    # Ensure n is odd and within the range
    if n % 2 == 0 or n < 1 or n > 19:
        return

    half_n = n // 2

    # Top half of the diamonds including the middle row
    for i in range(half_n + 1):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (half_n - i)
        print(f"{spaces}{stars}{spaces}{spaces}{stars}{spaces}")

    # Bottom half of the diamonds
    for i in range(half_n - 1, -1, -1):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (half_n - i)
        print(f"{spaces}{stars}{spaces}{spaces}{stars}{spaces}")


# Input
n = int(input())
print_diamonds(n)
