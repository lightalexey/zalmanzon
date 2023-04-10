a = 245690
b = 245756
n = 0
for i in range(a, b + 1):
    n += 1
    k = 0
    for d in range(2, i // 2 + 1):
        if i % d == 0:
            k += 1
            break
    if k == 0:
        print(n, i)
