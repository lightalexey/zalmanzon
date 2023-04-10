for i in range(289123456, 389123456):
    k = 0
    if i ** 0.5 == int(i ** 0.5):
        for d in range(2, int(i ** 0.5) + 1):
            if i % d == 0:
                k += 1
                if k == 1:
                    a = d

                if k > 2:
                    break
        if k == 2:
            print(i, i // a)
