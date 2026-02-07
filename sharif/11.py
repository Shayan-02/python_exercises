def count_unique_characters(name):
    """Count the number of unique characters in a name."""
    return len(set(name))


def find_name_with_max_unique_chars(names):
    """Find the name with the maximum number of unique characters."""
    max_unique_chars = 0
    for name in names:
        unique_chars = count_unique_characters(name)
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
    return max_unique_chars


# Read input
n = int(input())  # The first line contains the number of names
names = [input().strip() for _ in range(n)]  # The next n lines contain the names

# Find and print the result
print(find_name_with_max_unique_chars(names))
