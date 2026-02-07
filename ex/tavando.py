def find_next_power_of_two(n):
    power = 1
    while power <= n:
        power *= 2
    return power

n = int(input())
result = find_next_power_of_two(n)
print(result)
