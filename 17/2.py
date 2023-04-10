f = open('17 (1).txt')
s = [int(i) for i in f]
k = 0
maxim = 0
for i in range(len(s)-1):
    for d in range(i+1, len(s)):
        if s[i] % 160 != s[d] % 160 and (s[i] % 7 == 0 or s[d] % 7 == 0):
            k += 1
            n = s[i] + s[d]
            maxim = max(n, maxim)
print(k, maxim)