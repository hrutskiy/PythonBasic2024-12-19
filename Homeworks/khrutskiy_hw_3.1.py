num1 = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))
if operation == "+":
    result = num1 + num2
    print("Результат:", result)
elif operation == "-":
    result = num1 - num2
    print("Результат:", result)
elif operation == "*":
    result = num1 * num2
    print("Результат:", result)
elif operation == "/":
    if num2 != 0:  # Перевірка на ділення на 0
        result = num1 / num2
        print("Результат:", result)
    else:
        print("Помилка: ділення на 0 неможливе!")
