# گرفتن ورودی از کاربر
n = int(input("عدد n را وارد کنید: "))

# حلقه برای بررسی اعداد از 2 تا n
for num in range(2, n + 1):
    # فرض را بر اول بودن عدد می‌گذاریم
    is_prime = True
    # حلقه برای بررسی بخش پذیری عدد
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    # اگر عدد اول بود، آن را چاپ می‌کنیم
    if is_prime:
        print(num)
