for x in '0123456789ABCDE':
    a = int('123' + x + '5', 15) + int('1' + x + '233', 15)
    if a % 14 == 0:
        print(a // 14)