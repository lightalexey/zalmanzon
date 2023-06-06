for a in range(1000, 1, -1):
    k = True
    for x in range(1, 101):
        for y in range(1, 101):
            if not(((x <= 9) <= (x * x <= a)) * ((y * y <= a) <= (y <= 9))):
                k = False
                break
    if k == True:
        print(a)