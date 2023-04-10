for x in '012345678':
    for y in '012345678':
        a = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        if a % 61 == 0:
            print(a // 61)