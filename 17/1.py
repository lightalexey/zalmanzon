f = open('17.txt')
s = []
for i in range(5000):
    num = int(f.readline())
    s.append(num)
k = 0
maxim = -20000
for i in range(len(s) - 1):
    if s[i] % 3 == 0 or s[i+1] % 3 == 0:
        k += 1
        n = s[i] + s[i+1]
        maxim = max(n, maxim)
print(k, maxim)