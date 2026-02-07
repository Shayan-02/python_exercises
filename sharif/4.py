def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def convert_to_single_digit(n):
    while n >= 10:
        n = sum_of_digits(n)
    return n


# دریافت ورودی از کاربر
number = int(input())

# تبدیل عدد به عدد تک رقمی
result = convert_to_single_digit(number)

# چاپ نتیجه
print(result)
