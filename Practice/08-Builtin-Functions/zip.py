x = [1, 2, 3]
y = [4, 5, 6]
print(zip(x, y))
x = [1, 2, 3]
y = [4, 5, 6, 7, 8]
print(zip(x, y))
d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}
print(zip(d1, d2))
print(zip(d1, d2.itervalues()))

def switch(d1, d2):
    dout = {}
    for d1key, d2value in zip(d1, d2.itervalues()):
        dout[d1key] = d2value
    return dout
print(switch(d1, d2))
