import math


# Function to calculate e^x using Taylor series
def calculate_ex(x, n):
    ex = 1  # Start with the first term of the series (1)
    term = 1  # To keep track of each term in the series

    for i in range(1, n + 1):
        term *= x / i  # Calculate the next term (x^i / i!)
        ex += term  # Add the term to the result

    return ex


# Input handling
x = float(input())
n = int(input())

# Calculate e^x using the function
result = calculate_ex(x, n)

# Print the result rounded to three decimal places
print(f"{result:.3f}")
