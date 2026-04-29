str = 'This is bacon'
len_words = map(lambda x: len(x), str.split())
print(len_words)
len_words_solution = map(len, str.split())
print(len_words_solution)
num_list = [1, 2, 3, 4, 5]
num = reduce(lambda x, y: x * 10 + y, num_list)
print(num)
words = ['this', 'cow', 'fat', 'chicken', 'seen', 'cat']
c_words = filter(lambda x: x[0] == 'c', words)
print(c_words)

def concatenate(l1, l2, connector):
    return [x + connector + y for x, y in zip(l1, l2)]
print(concatenate(['get', 'you'], ['mad', 'skank'], '-'))

def swop_list(l):
    dout = {}
    for key, value in enumerate(l):
        dout[value] = key
    return dout
print(swop_list(['a', 'b', 'c']))
lst = ['a', 'b', 'c']
dict_list = {key: value for value, key in enumerate(lst)}
print(dict_list)
lst = [0, 1, 3, 4, 5, 5]
eq_index = len(filter(lambda x: x[0] == x[1], enumerate(lst)))
print(eq_index)
eq_index_solution = len([num for count, num in enumerate(lst) if num == count])
print(eq_index_solution)
