a = 174457
b = 174505
for i in range(a, b + 1):
    c = 0
    for d in range(2, i // 2 + 1):
        if i % d == 0:
            c += 1
        if c > 2:
            break
    if c == 2:
        # print(i)
        for m in range(2, i // + 1):
            if i % m == 0:
                print(m, end=' ')
        print()
