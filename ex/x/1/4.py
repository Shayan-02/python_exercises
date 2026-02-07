n = int(input("enter a number: "))


x, y = 1, 1

print(x, y, end=" ")
m = 3
while m <= n:
    x, y = y, x + y
    m += 1
    print(y, end=" ")