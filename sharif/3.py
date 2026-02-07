def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(a, b):
    start = min(a, b)
    end = max(a, b)
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

# دریافت ورودی از کاربر
a = int(input())
b = int(input())

# چاپ اعداد اول در محدوده
print_primes_in_range(a, b)
