def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2)
    if n > 0 and n % 2 == 1:
        return 1 + f(n - 1)


a = 0
for n in range(1000):
    if f(n) == 3:
        a += 1
print(a)
