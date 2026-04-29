list = [4, 56, 23, 453, 666, 23, 6789, 34]
print(reduce(lambda a, b: a if a > b else b, list))
print(reduce(lambda a, b: a + b, list))
