# Function to calculate and display the sum of numbers from 1 to n
def calculate_sum(n):
    if 1 <= n <= 1000:
        numbers = list(range(1, n + 1))  # Generate numbers from 1 to n
        sum_result = sum(numbers)  # Calculate the sum
        # Create a string with the summation process
        summation_string = " + ".join(map(str, numbers)) + " = " + str(sum_result)
        return summation_string
    else:
        return "Input must be between 1 and 1000"


# Example usage
n = int(input())  # Input from the user
print(calculate_sum(n))
