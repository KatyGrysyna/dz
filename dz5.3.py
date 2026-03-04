import string
text = input("Введіть текст:")

for ch in string.punctuation:
    text = text.replace(ch, "")
words = text.title().split()
hashtag = "#" + "".join(words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)


