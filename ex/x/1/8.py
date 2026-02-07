for a in range(10, 1001):
    prime = True
    for b in range(2, a):
        if a%b == 0:
            prime = False
            break
    if prime == 1:
        print(a, end="\t")