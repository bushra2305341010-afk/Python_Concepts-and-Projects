test_val = 0
while test_val < 10:
    if test_val in (1, 2, 3):
        test_val += 1
        continue
    elif test_val == 7:
        break
    print(test_val)
    test_val += 1
