st = 'Print only the words that start with s in this sentence'
st = st.split()
for item in st:
    if item[0] == 's':
        print(item)
print([x for x in range(11) if x % 2 == 0])
print(range(0, 11, 2))
div3 = [x for x in range(1, 51) if x % 3 == 0]
print(div3)
lst = []
st = 'Print every word in this sentence that has an even number of letters'
st = st.split()
for word in st:
    if len(word) % 2 == 0:
        lst.append(word)
print(lst)
lst2 = []
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        lst2.append('FizzBuzz')
    elif num % 3 == 0:
        lst2.append('Fizz')
    elif num % 5 == 0:
        lst2.append('Buzz')
    else:
        lst2.append(num)
print(lst2)
st = 'Create a list of the first letters of every word in this string'
lst3 = [x[0] for x in st.split()]
print(lst3)
