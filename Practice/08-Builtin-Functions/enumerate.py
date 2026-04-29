lst = ['a', 'b', 'c']
for number, item in enumerate(lst):
    print(number, item)
for count, item in enumerate(lst):
    if count >= 2:
        break
    else:
        print(item)
