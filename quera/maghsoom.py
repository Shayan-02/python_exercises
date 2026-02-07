def divisor_count_and_sum(n):
    total_count = 0
    total_sum = 0
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                total_count += 1
                total_sum += j
    
    return total_count, total_sum

# Read input
n = int(input())

# Get the result
count, sum_ = divisor_count_and_sum(n)

# Print the result
print(count, sum_)
