n = int(input())

total = 0
# جمع اعداد از 1 تا n
for i in range(1, n + 1):
    total += i
    # نمایش هر مرحله به صورت گام به گام
if i == n:
    print(f"{' + '.join(map(str, range(1, n+1)))} = {total}")

