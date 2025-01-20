import keyword
import string
user_input = input("Введіть ім'я змінної: ")
is_valid = True
if user_input in keyword.kwlist:
    is_valid = False
elif not user_input:
    is_valid = False
elif user_input == "__":
    is_valid = False
elif "__" in user_input:
    is_valid = False
elif user_input[0].isdigit():
    is_valid = False
else:
    allowed_chars = string.ascii_lowercase + string.digits + "_"
    for char in user_input:
        if char not in allowed_chars:
            is_valid = False
            break
print(is_valid)
