def ba():
    num1= input()
    if len(num1) != 8:
        print("invalid")
    else:
        for i in num1:
            if i not in ["0","1"]:
                print("invalid")

    num2 = input()
    if len(num2) != 8:
        print("invalid")
    else:
        for a in num2:
            if a not in ["0","1"]:
                print("invalid")
        
    count = 0
    for j in range(8):
        if num1[j] == 1 and num2[j] == 1:
            count += 1
    print(count)

ba()