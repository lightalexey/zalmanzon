f = open('17.txt')
s = f.read().split()
for i in range(len(s)):
    s[i] = int(s[i])
print(sum(s))
f.close()
# ------------------------------- 2 способ -------------------------
f = open('17.txt')
s = []
for i in range(5000):
    num = int(f.readline())
    s.append(num)
print(sum(s))
f.close()
# ------------------------------- 3 способ -------------------------
# f = open('17.txt')
# s = [int(i) for i in f]
s = [int(i) for i in open('17.txt')]
print(sum(s))
# close???
