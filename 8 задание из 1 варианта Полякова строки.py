k = 0
for a1 in 'polygn':
    for a2 in 'polygn':
        for a3 in 'polygn':
            for a4 in 'polygn':
                for a5 in 'polygn':
                    sl = a1 = a2 + a3 + a4 + a5
                    if sl[0] == sl[-1] and sl[1] == sl[-2] and (sl[3] == 'o' or sl[3] == 'y'):
                        k += 1
print(k)

k = 0
s = 'polygn'
for a1 in s:
    for a2 in s:
        for a3 in 'oy':
            for a4 in s:
                for a5 in s:
                    if a1+a2 == a5+a4: # and (a3 in 'oy'):
                        k += 1
print(k)