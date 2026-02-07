lst = []
while ans:=int(input()):
    if ans == 0:
        break
    else:
        lst.append(ans)

lst = lst[::-1]
print(lst)