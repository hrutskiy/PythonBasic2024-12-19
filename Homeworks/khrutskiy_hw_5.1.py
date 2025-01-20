import string
import keyword
user_input = input("Введіть ім'я змінної: ")
is_valid = True
if user_input in keyword.kwlist:
    is_valid = False
if user_input.count("__") > 0:
    is_valid = False
allowed_chars = string.ascii_lowercase + string.digits + "_"
for char in user_input:
    if char not in allowed_chars:
        is_valid = False
if user_input and user_input[0].isdigit():
    is_valid = False
if not user_input:
    is_valid = False
print(is_valid)
