def maghsoom(n):
    sum = count = 0
    for i in range(1, n + 1):
        for j in range(1, ((i + 1) // 2 + 2)):
            if i % j == 0:
                sum += j
                count += 1
        if i > 3:
            sum += i
            count += 1
    return count, sum


n = int(input())
count, sum = maghsoom(n)
print(count, sum)
