a = [1, 3, 5]
a = [6]
a = []

if a:
    result = sum(a[::2]) * a[-1]
else:
    result = 0
print(result)

