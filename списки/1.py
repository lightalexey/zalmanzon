# a1 a2 a3 
a = [] # a[1] a[2] a[i]
print(a)
n = int(input('Введи количество элементов:'))
for i in range(n):
    number = int(input('Введи число:'))
    a.append(number)
print('Исходный список:')
print(a)
print('Исходный список:')
for i in range(n):
    print(a[i], end=' ')