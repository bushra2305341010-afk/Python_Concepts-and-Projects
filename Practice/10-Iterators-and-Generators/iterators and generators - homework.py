from __future__ import print_function

def gen_square(num):
    for n in range(num):
        yield (n ** 2)
new = gen_square(5)
for _ in range(5):
    print(next(new), end=' ')
print('\n')
from random import randint

def rand_nums(n, low, high):
    for num in range(n):
        yield randint(low, high)
rand = rand_nums(5, 2, 9)
for _ in range(5):
    print(next(rand), end=' ')
print('\n')
s = 'hello'
s_gen = iter(s)
for letter in s_gen:
    print(letter, end='')
print('\n')
my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)
