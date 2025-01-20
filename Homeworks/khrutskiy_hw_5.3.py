user_input = input("Введіть рядок: ")
allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
cleaned_input = ''.join(char for char in user_input if char in allowed_characters)
words = cleaned_input.split()
hashtag = "#" + ''.join(word.capitalize() for word in words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print("Ваш хештег:", hashtag)