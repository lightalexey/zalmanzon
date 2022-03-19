# ax+b=0
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a != 0:
    d = b ** 2 + 4*a*c
    if d >= 0:
        x1 = -b + d**0.5 / 2 / a
        x2 = -b - d**0.5 / 2 / a
        print('корень уравнения x1=', x1)
        print('корень уравнения x2=', x2)
    else:
        print('действительных корней нет')
else:
    print('a=0')