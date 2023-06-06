for a in range(1000, 1, -1):
    k = 0
    for x in range(1, 101):
        if (not(x % a == 0)) <= ((x % 6 == 0) <= (x % 4 != 0)):
            k += 1
    if k == 100:
        print(a)
        break

for a in range(1000, 1, -1):
    k = True
    for x in range(1, 101):
        if not((not(x % a == 0)) <= ((x % 6 == 0) <= (x % 4 != 0))):
            k = False
            break
    if k:
        print(a)
        break