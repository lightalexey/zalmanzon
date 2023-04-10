a = 10**9
b = 10**9+1000
for i in range(a, b + 1):
    k = True
    for d in range(2, int(i**0.5) + 1):
        if i % d == 0:
            k = False
            break
    if k:
        print(i)
