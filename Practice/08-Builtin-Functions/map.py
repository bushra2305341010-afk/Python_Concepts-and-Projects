def farenheit(T):
    return 9.0 / 5 * T + 32
temps = [0, 22.5, 40, 100]
print(map(farenheit, temps))
print(map(lambda T: 9.0 / 5 * T + 32, temps))
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print(map(lambda x, y, z: x + y + z, a, b, c))
