alf = 'ТИМОФЕЙ'
k = 0
for i1 in alf:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    sl = i1 + i2 + i3 + i4 + i5
                    if sl.count('Т') >= 1 and sl.count('Й') <= 1:
                        k += 1
print(k)