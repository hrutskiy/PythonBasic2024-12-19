
a = [0, 1, 0, 12, 3]
a = [0]
a = [1, 0, 13, 0, 0, 0, 5]
[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1]

new_list = list(a)
zero_count = a.count(0)
for num in a:
    if num == 0:
        new_list.remove(num)
new_list.extend([0] * zero_count)
print(new_list)



