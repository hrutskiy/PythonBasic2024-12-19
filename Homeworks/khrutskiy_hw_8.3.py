from collections import Counter

def find_unique_value(some_list):
    counts = Counter(some_list)
    for key, value in counts.items():
        if value == 1:
            return key


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")