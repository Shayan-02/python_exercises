"""
tas aghaye jalalian
"""
dice_number = int(input())
# print(7 - dice_number)

if dice_number in range(1, 7): # if 0 < dice_number < 7
    if dice_number == 1:
        print(6)
    elif dice_number == 2:
        print(5)
    elif dice_number == 3:
        print(4)
    elif dice_number == 4:
        print(3)
    elif dice_number == 5:
        print(2)
    elif dice_number == 6:
        print(1)
