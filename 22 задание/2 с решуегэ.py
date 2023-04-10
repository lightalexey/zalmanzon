for x in range(1,1000):
    a = 0
    b = 0
    xx = x
    while x > 0:
       a += 1
       b = b + x % 100
       x = x//100
    if a == 2 and b == 13:
        print(xx)