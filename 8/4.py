a = 0
alphabet = '0123456789ab'

for i in range(100000, 1000001):
    k = i
    n = ''
    while k != 0:
        n = str(k % 12) + n
        k //= 12
    if k % int(n[1], 12) == 0:
        a += 1
print(a)