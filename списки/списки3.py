a = [5, 450, 78, -4, 0, 12, 0, 89, 125, 4]
# сумму нечетны элементов с четными индексами
k = 0
for i in range(len(a)):
    if i % 2 == 0 and a[i] % 2 == 1:
        k += a[i]
print(k)
# максимальный элемент среди элементов с четными индексами
maxim = a[0]
for i in range(len(a)):
    if i % 2 == 0 and a[i] > maxim:
        maxim = a[i]
print(maxim)
# Три подряд идущих элементов, сумма которых максимальна
b = a[0]
c = a[1]
d = a[2]
for i in range(len(a) - 2):
    if a[i] + a[i+1] + a[i+2] > b + c + d:
        b = a[i]
        c = a[i+1]
        d = a[i+2]
print(b, c, d)