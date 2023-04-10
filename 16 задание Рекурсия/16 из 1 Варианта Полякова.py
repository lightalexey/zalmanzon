def f(n):
    if (n ** 0.5).is_integer():
       return n ** 0.5
    else:
        return f(n + 1) + 1
print(f(4850) + f(5000))

def g(n):
    a = str(n ** 0.5)
    if a[:-2:] == '.0':
        return n ** 0.5
    else:
        return f(n+1) + 1
print(g(4850) + g(5000))

# if a == int(a): - число целое