def mashgh(x1, x2, x3):

    if sum([x1, x2, x3]) == 180 and all(x > 0 for x in [x1, x2, x3]):
        return "Yes"
    else:
        return"No"

a1, a2, a3 = map(int, input().split())
print(mashgh(a1, a2, a3))
