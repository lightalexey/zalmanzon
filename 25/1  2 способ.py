a = 174457
b = 174505
for i in range(a, b + 1):
    c = 0
    for d in range(2, i // 2 + 1):
        if i % d == 0:
            c += 1
            if c == 1:
                del1 = d
        if c > 2:
            break
    if c == 2:
        print(del1, i / del1, end=' ')
        print()
