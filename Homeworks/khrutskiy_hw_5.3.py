import string

user_input = input("Введіть рядок: ")
cleaned_input = ''.join(char if char not in string.punctuation else ' ' for char in user_input)
words = cleaned_input.split()
hashtag = ''.join(word.capitalize() for word in words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
hashtag = '#' + hashtag
print(hashtag)
