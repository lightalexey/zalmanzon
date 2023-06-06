a = input()
k = 0
for i in a:
    k += int(i)
print(k)
# 2 способ
k = 0
b = int(a)
while b != 0:
    k += b % 10
    b //= 10
print(k)