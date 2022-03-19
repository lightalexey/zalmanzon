a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a < b + c:
    if b < a + c:
        if c < a + b:
            print('треугольник существует')
        else:
            print('треугольника нет')
    else:
        print('треугольника нет')
else:
    print('треугольника нет')
