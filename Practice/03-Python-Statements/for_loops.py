str = 'this is a string'
for letter in str:
    print(letter)
t = ((1, 2), (3, 4), (5, 6))
for tup in t:
    print(tup)
for t1, t2 in t:
    print(t1)
d = {'key1': 1, 'key2': 2, 'key3': 3}
for item in d:
    print(item)
for j, k in d.items():
    print('{a} , {b}'.format(a=j, b=k))
    print('{0} , {1}'.format(j, k))
    print('%s , %d' % (j, k))
