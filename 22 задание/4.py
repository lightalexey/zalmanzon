for x in range(10000, 1, -1):
    L = 0
    M = 0
    xx = x
    while x > 0:
        L += 1
        if x % 2 == 0:
            M = M + (x % 10) // 2
        x = x // 10
    if L == 3 and M == 7:
        print(xx)
        break