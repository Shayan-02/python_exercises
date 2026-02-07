def count_o(n):
    a = "Wow!"
    b = "o" * n
    a = a[:1] + b + a[1:]
    return a

n = int(input())

print(count_o(n-1))