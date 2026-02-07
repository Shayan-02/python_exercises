def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    primes = []
    for num in range(start + 1, end):
        if is_prime(num):
            primes.append(num)
    return primes



start = int(input())
end = int(input())

# اعداد اول بین این دو عدد
primes = find_primes_in_range(start, end)

if primes:
    print(",".join(map(str, primes)))