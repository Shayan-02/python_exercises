n = int(input())

s = n * (n + 1) // 2

for i in range(1, n + 1):
    print(i, end='')
    if i < n:
        print(' + ', end='')

print(' =', s)
