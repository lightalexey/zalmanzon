a = [5, 4, 7, -4, 0, 1, 0, 8, -12, 4]
k = 0
# количество пар соседних элементов сумма которых четна
for i in range(1, len(a)):
    if (a[i - 1] + a[i]) % 2 == 0:
        k += 1
print(k)
k = 0
for i in range(len(a)-1):
    if (a[i] + a[i+1]) % 2 == 0:
        k += 1
print(k)
# количество пар соседних элементов среди которых хотя бы один четный
k = 0
for i in range(len(a)-1):
    if a[i] % 2 == 0 or a[i+1] % 2 == 0:
        k += 1
print(k)
a = [1, 2, 3, 4]
k = 0
# количество пар элементов сумма которых четна
for i in range(len(a)):
    for d in range(i + 1, len(a)):
        if (a[i] + a[d]) % 2 == 0:
            k += 1
print(k)


