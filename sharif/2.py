def calculate_remainder(n):
    if n < 0:
        return calculate_remainder(-n)

    remainder = 0
    i = 0
    while n > 0:
        remainder += (-1) ** i * (n % 10)
        n //= 10
        i += 1

    if remainder < 0:
        remainder += 11

    return remainder % 11


number = 145
remainder = calculate_remainder(number)
print(f"baghimandeh {number} bar 11 : {remainder}")
