test_list = [
    [12, 3, 4, 10],
    [1],
    [],
    [12, 3, 4, 10, 8]
]
for lst in test_list:
    if len(lst) > 1:
        lst = [lst[-1]] + lst[:-1]
    print(lst)