test_val = 0
while test_val < 3:
    print(test_val)
    test_val += 1
else:
    print('Finished')
for k in range(1, 5):
    for i in (1, 2, 3):
        if i == k:
            print('%d - True' % k)
            break
    else:
        print('%d - False' % k)
