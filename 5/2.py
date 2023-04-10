for n in range(10000):
    r = bin(n)[2:].replace('0', '*').replace('1', '0').replace('*', '1')
    r = int(r, 2)
    if n - r == 979:
        print(n)

