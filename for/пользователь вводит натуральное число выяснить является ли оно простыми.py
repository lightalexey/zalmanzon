a = int(input())

# b = 2
# while b < a:
#     if a % b != 0:
#         b += 1
#     else:

b = 0
for i in range(1, a + 1):
    if a % i == 0:
        b += 1
if b == 2:
    print(a, " простое число")
else:
    print(a, " составное число")

b = 0
for i in range(2, a // 2 + 1):
    if a % i == 0:
        b += 1
if b == 0:
    print(a, " простое число")
else:
    print(a, " составное число")

b = 0
for i in range(2, a // 2 + 1):
    if a % i == 0:
        b += 1
if b:
    print(a, " составное число")
else:
    print(a, " простое число")

b = True
for i in range(2, a // 2 + 1):
    if a % i == 0:
        b = False
        break
if b:
    print(a, " простое число")
else:
    print(a, " составное число")