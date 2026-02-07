def is_right_triangle(a, b, c):
    # Check if the three sides can form a right triangle
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "YES"
    else:
        return "NO"

# Get input from the user
a = int(input())
b = int(input())
c = int(input())

# Check and print if they form a right triangle
print(is_right_triangle(a, b, c))
