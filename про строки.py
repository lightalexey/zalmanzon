s = 'преступление и наказание'
k = 0
for i in s:
    if i == 'е':  # if i in 'аоеуыэя'
        k += 1
print(k)
k = s.count('е')
s = s.replace('п', 'П', 1)
print(s)
s = 'П' + s[1:]