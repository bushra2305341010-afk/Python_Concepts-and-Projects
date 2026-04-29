import math

def vol(rad):
    return 4 / 3 * math.pi * rad ** 3
print(vol(5))

def ran_check(num, low, high):
    if num in range(low, high + 1):
        return True
    return False
print(ran_check(5, 6, 10))
print(ran_check(10, 6, 10))

def up_low(s):
    count = {'upper': 0, 'lower': 0}
    for letter in s:
        if letter.islower():
            count['lower'] += 1
        elif letter.isupper():
            count['upper'] += 1
    print('Upper: ', count['upper'])
    print('Lower: ', count['lower'])
up_low('This is B')
l = [1, 1, 1, 1, 2, 3, 3, 4, 4, 4, 5]

def unique_list(lst):
    temp = []
    for num in set(lst):
        temp += [num]
    return temp
print(unique_list(l))

def unique_list2(lst):
    return list(set(lst))
print(unique_list2(l))

def multiply(numbers):
    mult = numbers[0]
    for num in range(1, len(numbers)):
        mult *= numbers[num]
    return mult
print(multiply([1, 2, 3, 4]))

def palindrome(s):
    test = ''
    for word in s.split():
        test += word
    if test == test[::-1]:
        return True
    else:
        return False
print(palindrome('Test Files case'))
print(palindrome('nurses run'))

def palindrome_sug(s):
    s = s.replace(' ', '')
    return s == s[::-1]
print(palindrome_sug('nurses run'))
import string

def is_pangram(s, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    alphaset.add(' ')
    return alphaset <= set(s.lower())
print(is_pangram('the quick brown fox jumps over the lazy 123456789'))
print(is_pangram('the quick brown fox jumps over the lazy dog'))
print(is_pangram('thequickbrownfoxjumpsoverthelazydog!'))
