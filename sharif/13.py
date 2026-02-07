def count_eyewitnesses(first_row, second_row):
    count = 0
    for i in range(8):
        if second_row[i] == 1 and first_row[i] == 1:
            count += 1
    return count

# Example usage
# دریافت ورودی از کاربر به صورت یک خط
input_line1 = input()
input_line2 = input()

# تبدیل ورودی به لیست از طریق جدا کردن اعداد با استفاده از فاصله
list1 = input_line1.split()
list2 = input_line2.split()

# تبدیل عناصر لیست به اعداد صحیح
list1 = [int(x) for x in list1]
list1 = [int(bool(x)) for x in list1]
list2 = [int(x) for x in list2]
list2 = [int(bool(x)) for x in list2]

# چاپ لیست نهایی
print(count_eyewitnesses(list1, list2))
