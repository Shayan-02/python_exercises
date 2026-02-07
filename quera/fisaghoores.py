deg = input().split()

deg_int = [int(i) for i in deg]

if deg_int[0] > 0 and deg_int[1] > 0 and deg_int[2] > 0:
    if deg_int[0] + deg_int[1] + deg_int[2] == 180:
        print("Yes")
    else:
        print("No")
else:
    print("No")