for i in range(302300, 10 ** 10, 3023):
    a = str(i)
    if a[0] == '1' and a[2:5] == '954' and a[-2:] == '21':
        print(i)
print('--------------- 2 способ ------------------')
for i in range(302300, 10 ** 10, 3023):
    a = str(i)
    if a[0] == '1' and '954' in a and a.index('954') == 2 and a[-2:] == '21':
        print(i)