for n in range(1, 100):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r[1:]
    else:
        r = '1' + r + '00'
    if r.count('1') % 2 == 0:
        r = r[1:]
    else:
        r = '1' + r + '00'
    r = int(r, 2)
    if r > 100:
        print(n)
