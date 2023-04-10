num = 170
ss = 16
a = ''
while num != 0:
    ost = num % ss
    if ost == 10:
            ost = 'A'
    if ost == 11:
            ost = 'B'
    if  ost == 12:
            ost = 'C'
    if ost == 13:
            ost = 'D'
    if ost == 14:
            ost = 'E'
    if ost == 15:
            ost = 'F'
    a += str(ost) # a = str(ost) + a
    num //= ss

a = a[::-1]
print(a)
