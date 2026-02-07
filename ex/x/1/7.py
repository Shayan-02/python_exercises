f1 = 1
f2 = 1

n = int(input("enter a number: "))
print(f1, f2)
for i in range(n):
    f3 = f1 + f2
    f1, f2 = f2, f1 + f2
    print(f3)
