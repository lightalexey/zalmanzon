for n in range(100):
    n = bin(n)[2:]
    n += str((n.count('1') % 2))
    n += str((n.count('1') % 2))
    r = int(n, 2)
    if r > 43:
        print(r)
