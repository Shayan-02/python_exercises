def khosh(n: int)-> str:
    """
    This function prints "man khoshghlab hastam" (I am happy) n times.
    If n is less than 1, it prints "invalid" instead.
    """
    if n < 1:
        print("invalid")  # n is less than 1, print "invalid"
    else:
        for i in range(n):
            print("man khoshghlab hastam")  # print "man khoshghlab hastam" n times


n = int(input())
khosh(n)