a = [5, 45, 78, -4, 0, 12, 0, 89, -125, 4]
k = 0
n = 0
for i in range(len(a)):
    if a[i] > a[k]:
        k = i
    if a[i] < a[n]:
        n = i
print(a[k], k)
print(a[n], n)
b = a[0]
a[0] = a[-1]
a[-1] = b
print(a)
print(*a)
a[0], a[-1] = a[-1], a[0]
print(a)
a[k], a[n] = a[n], a[k]
print(a)

