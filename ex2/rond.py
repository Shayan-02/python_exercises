def is_ronde(phone_number):
    # ویژگی اول: بررسی اینکه آیا حداقل یک رقم ۴ بار یا بیشتر تکرار شده است
    for digit in "0123456789":
        if phone_number.count(digit) >= 4:
            return "Ronde!"

    # ویژگی دوم: بررسی اینکه آیا سه رقم متوالی مشابه وجود دارد
    for i in range(6):  # آخرین سه رقم متوالی تا ایندکس 5 می‌تواند باشد
        if phone_number[i] == phone_number[i + 1] == phone_number[i + 2]:
            return "Ronde!"

    # ویژگی سوم: بررسی اینکه آیا شماره آینه‌ای است
    if phone_number == phone_number[::-1]:
        return "Ronde!"

    # اگر هیچ کدام از ویژگی‌ها نبود، "Rond Nist"
    return "Rond Nist"


# ورودی
t = int(input())  # تعداد شماره‌ها
phone_numbers = [input().strip() for _ in range(t)]  # دریافت تمام شماره‌ها

# پردازش شماره‌ها و ذخیره نتایج
results = [is_ronde(phone_number) for phone_number in phone_numbers]

# نمایش تمام نتایج
for result in results:
    print(result)
