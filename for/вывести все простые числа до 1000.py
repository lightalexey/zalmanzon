for a in range(2, 1000):
    b = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            b += 1
    if b == 0:
        print(a, end=' ')

