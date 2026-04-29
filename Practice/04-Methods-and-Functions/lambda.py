def square(num):
    return num ** 2
square = lambda num: num ** 2
print(type(square))
print(square(2))
even = lambda x: x % 2 == 0
print(even(2), even(3))
first = lambda s: s[0]
print(first('Hello'))
rev = lambda s: s[::-1]
print(rev('Hello'))
adder = lambda x, y: x + y
print(adder(2, 4))
new_list = [(lambda x: x * 3)(num) for num in range(5)]
print(new)
