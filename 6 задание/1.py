k = 0
for x in range(1, 10):
    for y in range(1, 10):
        # if y > 1 / 3 ** 0.5 * x and y < - 1 / 3 ** 0.5 * x + 10:
        if 1 / 3 ** 0.5 * x < y < - 1 / 3 ** 0.5 * x + 10:
            k += 1
print(k)