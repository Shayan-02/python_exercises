def barnameh(n: int, l: int, r: int) -> int:
    day = n // r
    if n < l or n < r or day * l > n:
        return -1
    if n % r != 0:
        day += 1
    return day


n = int(input())
l, r = map(int, input().split())

print(barnameh(n, l, r))
