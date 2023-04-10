a = [5, 45, 78, -4, 0, 12, 0, 89, -125, 4]
k = 0
n = 0
maxim = a[0]
minim = a[0]
for i in range(len(a)):
    if a[i] > maxim:
        maxim = a[i]
        k = i
    if a[i] < minim:
        minim = a[i]
        n = i
print(maxim, k)
print(minim, n)
print(max(a), min(a))

