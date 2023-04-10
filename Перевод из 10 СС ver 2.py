num = 170
ss = 16
a = ''
alphabet = '0123456789ABCDEF'
while num != 0:
    a += alphabet[num % ss]
    num //= ss
a = a[::-1]
print(a)
