a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a < b + c and b < a + c and c < b + a:
    # print('треугольник существует')
    if a == b and b == c and a == c:
        print('треугольник равносторонний')
    else:
        if a == b or b == c or a == c:
            print('треугольник равнобедренный')
        else:
            if a ** 2 + b ** 2 == c ** 2 or c ** 2 + b ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
                print('теугольник прямоугольный')
            else:
                print('треугольник произвольный')
else:
    print('треугольника нет')
