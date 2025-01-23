number = int(input("Введіть ціле число: "))
while number > 9:
    product = 1
    for digit in str(number):
        product *= int(digit)
    number = product
print(number)
