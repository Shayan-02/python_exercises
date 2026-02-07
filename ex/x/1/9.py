def next_greater_permutation(x):
    digits = list(str(x))
    n = len(digits)

    # Step 2: Find the first digit that can be increased by reordering
    for i in range(n - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        # If no such digit is found, return 0
        return 0

    # Step 3: Find the smallest digit on the right of the found digit and larger than it
    for j in range(n - 1, i, -1):
        if digits[j] > digits[i]:
            break

    # Step 4: Swap the found digits
    digits[i], digits[j] = digits[j], digits[i]

    # Step 5: Sort the digits to the right of the found position
    digits = digits[:i + 1] + sorted(digits[i + 1:])

    # Combine digits back to a number
    next_number = int("".join(digits))
    return next_number

# Example usage
x = int(input().strip())
print(next_greater_permutation(x))
