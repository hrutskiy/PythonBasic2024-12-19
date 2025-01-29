def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
    Генератор, який повертає n елементів числової послідовності,
    де кожен наступний елемент обчислюється за переданою функцією.

    :param begin: перший елемент послідовності
    :param end: кількість елементів у послідовності
    :param func: функція, яка формує значення для послідовності
    """
    current = begin
    for _ in range(end):
        yield current
        current = func(current)

from inspect import isgenerator


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')
