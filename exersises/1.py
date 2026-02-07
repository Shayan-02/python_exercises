class CustomError(Exception):
    pass


# Example 1: Handling ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")

# Example 2: Handling IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"Index error: {e}")

# Example 3: Handling KeyError
try:
    d = {"name": "Ali"}
    print(d["age"])
except KeyError as e:
    print(f"Key error: {e}")

# Example 4: Handling multiple exceptions
try:
    x = int("hello")
except (ValueError, TypeError) as e:
    print(f"Value or Type error: {e}")

# Example 5: Using else and finally in exception handling
try:
    num = int("10")
    print("Conversion successful.")
except ValueError as e:
    print(f"Value error: {e}")
finally:
    print("This block always executes.")

# Example 6: Custom exception and using raise
try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(f"Custom error: {e}")

# Example 7: Using raise to propagate errors
try:
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print("Handling ZeroDivisionError, but raising it again.")
        raise
except Exception as e:
    print(f"Final error: {e}")
