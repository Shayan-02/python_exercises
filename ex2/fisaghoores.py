f = [int(input()) for _ in range(3)]

if f[0]**2 + f[1]**2 == f[2]**2 or f[0]**2 + f[2]**2 == f[1]**2 or f[1]**2 + f[2]**2 == f[0]**2:
    print("YES")
else:
    print("NO")