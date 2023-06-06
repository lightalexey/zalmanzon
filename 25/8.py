for i in range(95632, 95651):
    k = 0
    for d in range(1, i + 1, 2):
        if i % d == 0 and d % 2 == 1:
            k += 1
        if k > 6:
            break
    if k == 6:
        for d in range(1, i + 1):
            k = 0
            if i % d == 0 and d % 2 == 1:
                print(d, end=' ')
        print()
