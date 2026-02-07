lst = []

r = True

while r:
    a = int(input())
    if a == 0:
        r = False
        lst.reverse()
    else:
        lst.append(a)
    
print(lst)