import math

def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            print('not prime')
            break
    else:
        print('prime')
is_prime(16)

def is_prime2(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
print(is_prime2(16))
