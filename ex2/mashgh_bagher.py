lst = input().split()

for _ in range(len(lst)):
    lst[_] = int(lst[_])

sums = 0
for _ in range(3):
    if lst[_] == 0:
        print("No")
    else:
        sums += lst[_]

if sums == 180:
    print("Yes")
else:
    print("No")