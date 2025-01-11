a = [0, 1, 0, 12, 3]
a = [0]
a = [1, 0, 13, 0, 0, 0, 5]
a = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
zero_count = a.count(0)
i = 0
while i < len(a):
    if a[i] == 0:
        del a[i]
    else:
        i += 1
a.extend([0] * zero_count)
print(a)