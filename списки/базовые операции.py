from random import randrange
a = [] 
n = 100
print('Исходный список:')
for i in range(n):
    a.append(randrange(-50,50))
    print(a[i], end=' ')
print()
# код начинается отсюда...
summa = 0
pr = 1
k2 = 0
kpol = 0
spol=0
z=0
for i in range(n):
    summa = summa + a[i]
    pr = pr * a[i]
    if a[i] % 2 == 0:
        k2 += 1  # k2 = k2 + 1 k2++
    if a[i] > 0:
        kpol = kpol + 1
        spol = spol + a[i]
    if a[i] == 0:
        z += 1

print('сумма всех элементов списка равна', summa)
print('произведение элементов равно', pr)
print(k2)
print('количество положительных элементов равно', kpol)
print(spol)
print(z)
sred = summa / n
print(sred)

