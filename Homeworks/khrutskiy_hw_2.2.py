number = int(input("Введіть п'ятизначне число: "))
digit1 = number % 10              # Остання цифра
digit2 = (number // 10) % 10      # Четверта цифра
digit3 = (number // 100) % 10     # Третя цифра
digit4 = (number // 1000) % 10    # Друга цифра
digit5 = (number // 10000) % 10   # Перша цифра
reversed_number = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5
print("Перевернуте число:", reversed_number)
