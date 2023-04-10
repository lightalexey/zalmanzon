for n in range(1000):
    r = ''
    t = n
    while t != 0:
        r = str(t % 3) + r
        t //= 3
    r += str(n % 3)
    r = int(r, 3)
    if r >= 1000:
        print(r)
