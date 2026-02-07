# تعداد اولیه متغیر
result = 0
# حلقه اصلی
while True:
    # گزینه های منو
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Close Calculator")
    # ورودی کاربر رو بگیر
    choice = input("Enter your choice: ")
    # محاسبه طبق انتخاب کاربر
    if choice == "1":
        num = float(input("Enter number to add: "))
        result += num
        print("Result: ", result)
    elif choice == "2":
        num = float(input("Enter number to subtract: "))
        result -= num
        print("Result: ", result)
    elif choice == "3":
        num = float(input("Enter number to multiply: "))
        result *= num
        print("Result: ", result)
    elif choice == "4":
        num = float(input("Enter number to divide: "))
        if num != 0:
            result /= num
            print("Result: ", result)
        else:
            print("Cannot divide by zero!")
    elif choice == "5":
        print("Closing calculator...")
        break
    else:
        print("Invalid choice. Please try again.")
