lst1 = [x for x in 'word']
print(lst1)
lst2 = [x ** 2 for x in range(1, 6)]
print(lst2)
lst3 = [x for x in range(11) if x % 2 == 0]
print(lst3)
lst4 = [x ** 2 for x in [x ** 2 for x in range(1, 6)]]
print(lst4)
celsius = [0, 10, 20.1, 34.5]
fahrenheit = [32 + temp * (float(9) / 5) for temp in celsius]
print(fahrenheit)
