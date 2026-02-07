def calculator(n: int, m: int, li: list[int]) -> int:
    """
    This function divides a list into groups and calculates the sum of each group.
    It then computes the final value based on alternating addition and subtraction of group sums.

    Parameters:
        n (int): The length of the list.
        m (int): The size of each group.
        li (list): The list to be divided into groups.

    Returns:
        int: The final value after alternating addition and subtraction of group sums.
    """
    # Step 1: Divide the list into groups and calculate the sum of each group
    group_sums = []
    for i in range(0, n, m):
        group_sum = sum(li[i : i + m])
        group_sums.append(group_sum)

    # Step 2: Compute the final value based on alternating addition and subtraction of group sums
    result = 0
    for i in range(len(group_sums)):
        if i % 2 == 0:
            result += group_sums[i]
        else:
            result -= group_sums[i]

    return result



# Input
# n, m = map(int, input().split())
# li = list(map(int, input().split()))

# Calling the function and displaying the result
print(calculator(int(input()), int(input()), input().split()))  # Output should be 6
