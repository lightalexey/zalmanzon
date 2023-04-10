alf = '01234567'
k = 0
for i1 in alf[1:]:
    for i2 in alf:
        for i3 in alf:
            for i4 in alf:
                for i5 in alf:
                    sl = i1 + i2 + i3 + i4 + i5
                    if sl.count('6') == 1:
                        n = sl.find('6')
                        if n > 0 and n < 4:
                            if int(sl[n-1]) % 2 != 1 and int(sl[n+1]) % 2 != 1:
                                k += 1
                        if n == 0:
                            if int(sl[n+1]) % 2 != 1:
                                k += 1
                        if n == 4:
                            if int(sl[n-1]) % 2 != 1:
                                k += 1
print(k)
