for i in range(1,1000):
    a = 0
    b = 0
    x = i
    while x > 0:
       a += 1
       if b < (x % 8):
           b =x % 8
       x //= 8
    if a == 3 and b == 2:
        print(i)