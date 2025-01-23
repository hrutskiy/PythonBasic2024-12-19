seconds_input = int(input("Введіть кількість секунд (0-8639999): "))
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR
days = seconds_input // SECONDS_IN_DAY
remaining_seconds = seconds_input % SECONDS_IN_DAY
hours = remaining_seconds // SECONDS_IN_HOUR
remaining_seconds %= SECONDS_IN_HOUR
minutes = remaining_seconds // SECONDS_IN_MINUTE
seconds = remaining_seconds % SECONDS_IN_MINUTE
if 11 <= days % 100 <= 14:
    day_word = "днів"
elif days % 10 == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4:
    day_word = "дні"
else:
    day_word = "днів"
result = f"{seconds_input} -> {days} {day_word}, {hours:02}:{minutes:02}:{seconds:02}"
print(result)