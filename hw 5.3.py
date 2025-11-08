import string

text = input("Введіть рядок: ")

for ch in string.punctuation:
    text = text.replace(ch, "")

words = text.split()
hashtag = "#" + "".join(word.capitalize() for word in words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

if hashtag == "#":
    print("")
else:
    print(hashtag)
