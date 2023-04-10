alf = 'ABCDX'
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                sl = i1 + i2 + i3 + i4
                if sl.count('X') == 1:
                    k += 1
print(k)