x = 6
while 2 + 5 * x != 47:
    x += 1
print(x)

for i in range(6, 100):
    if 2 + 5 * i == 47:
        print(i)
        break

print(bin(123))
print(bin(123)[2:])
print(oct(123))
print(hex(123))

print(int('1234', 5))
# print(int('1234', 4)) ОШИБКА!
print(int('1234', 16))
print(int('AA', 16))
print(int('1234', 36))
# print(int('1234', 37)) Не. ТОЛько до 36
print(int('35', 36))
print(int('Z', 36))
