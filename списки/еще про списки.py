a = [5, 45, 78, -4, 0, 12, 0, 89, -125, 4]
s = 0
p = 1
k = 0
n = 0
b = 0
m = 0
print(len(a), a[0], a[-1])
for i in range(len(a)):
    s += a[i]
    if a[i] != 0:
        p *= a[i]
    else:
        k += 1
print(s, p)
s = 0
for i in a:
    if i % 2 == 0:
        n += 1
    if i > 0:
        b += i
        m += 1
    s += i
print(b / m)
print(s)
print(sum(a))

