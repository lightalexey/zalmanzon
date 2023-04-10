f = open('24_demo.txt')
s = f.read()
# print(len(s))
k = 1
tek = 1
for i in range(len(s)-1):
    if s[i] != s[i+1]: # текущая цепочка растёт...
        tek += 1
    else: # цепочка оборвалась
        k = max(k, tek)
        tek = 1
if tek > k:
    k = tek
print(k)

# print(len(max(s.replace('XX', ' ').replace('ZZ', ' ').replace('YY', ' ').split())))
