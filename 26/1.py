f = open('26_demo (1).txt')
summa, k = f.readline().split()
summa, k = int(summa), int(k)
#data = f.read().split()
#for i in range(len(data)):
#    data[i] = int(data[i])

#data = f.readlines()
#for i in range(len(data)):
#    data[i] = int(data[i])

#data = []
#for i in range(k):
#    number = int(f.readline())
#    data.append(number)
data = [int(i) for i in f]
print(data)
data.sort()
#data = sorted(data)
print(data)
a = 0
n = 0
for i in range(k):
    a += data[i]
    if a > summa:
        a -= data[i]
        break
    n += 1
print(n)
delta = a - data[n]

while True:
    