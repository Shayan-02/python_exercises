# تابعی برای تبدیل عدد a به مبنای b
def to_base_a(a, b):
    result = []
    while a > 0:
        result.append(a % b)
        a = a // b
    return result[::-1]  # بازگشت لیست از آخر به اول


# دریافت ورودی
a, b = map(int, input().split())

# تبدیل a به مبنای b
c = to_base_a(a, b)

# محاسبه sum1 و sum2
sum1 = 0
sum2 = 0

# ارقام با ارزش‌ترین رقم (سمت چپ‌ترین) را برای sum1 جمع می‌کنیم
for i in range(0, len(c), 2):
    sum1 += c[i]

# بقیه ارقام را برای sum2 جمع می‌کنیم
for i in range(1, len(c), 2):
    sum2 += c[i]

# مقایسه sum1 و sum2
if sum1 == sum2:
    print("Yes")
else:
    print("No")
