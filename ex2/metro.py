a = input().split()
b = input().split()

c = 0
for i in range(8):
    if a[i] == b[i] == "1":
        c += 1

print(c)