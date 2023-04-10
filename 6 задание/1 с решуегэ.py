for s in range(1, 1000):
    x = s
    s = (s - 21) // 10
    n = 1
    while s > 0:
        n = n * 2
        s = s - n
    if n == 32:
        print(x)

