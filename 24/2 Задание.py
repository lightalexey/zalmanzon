f = open('24_demo (1).txt')
tec = 1
k = 1
s = f.read()
for i in range(len(s)-1):
    if s[i] == 'X' and s[i+1] == 'X':
        tec += 1
    else:
        if tec > k:
            k = tec
        tec = 1
print(max(k, tek))