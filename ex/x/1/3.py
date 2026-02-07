n = int(input("enter a number: "))

f1 = 1
f2 = 1
f = 0

print(f1)
print(f2)
while f <= n:
    f = f1 + f2
    f1 = f2
    f2 = f
    if f <= n:
        print(f)