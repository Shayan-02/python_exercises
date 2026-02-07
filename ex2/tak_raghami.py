a = int(input())


while a >= 10:
    a = sum(int(digit) for digit in str(a))

print(a)