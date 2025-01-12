test_list = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1],
    []
    ]
for lst in test_list:
    a = (len(lst) + 1) // 2
    separated_lst = [lst[:a], lst[a:]]
    print(separated_lst)