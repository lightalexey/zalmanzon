for a in range(6, 10**9):
    b = 0
    for i in range(1, a // + 1):
        if a % i == 0:
            b += i
    if a == b:
        print(a)
