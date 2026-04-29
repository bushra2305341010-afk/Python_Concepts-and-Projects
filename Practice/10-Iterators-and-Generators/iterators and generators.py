def gencubes(num):
    for num in range(num):
        yield (num ** 3)
for x in gencubes(10):
    print(x)
print('\n')

def simple_gen():
    for x in range(3):
        yield x
g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
s = 'hello'
for let in s:
    print(let)
s_iter = iter(s)
print(next(s_iter))
