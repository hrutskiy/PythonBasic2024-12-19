import keyword
import string
user_input = input("Введіть ім'я змінної: ")
is_valid = True
if user_input in keyword.kwlist:
    is_valid = False
elif user_input[0].isdigit():
    is_valid = False
elif any(char.isupper() for char in user_input):
    is_valid = False
elif any(char in string.punctuation.replace("_", "") for char in user_input) or " " in user_input:
    is_valid = False
elif user_input.count("_") > 1 and all(char == "_" for char in user_input):
    is_valid = False
elif not user_input:
    is_valid = False
print(is_valid)