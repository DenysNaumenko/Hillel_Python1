import string
import keyword

user_input = input("Please enter string: ")

if not user_input:
    print(False)
elif user_input[0].isdigit():
    print(False)
elif any(ch.isupper() for ch in user_input):
    print(False)
elif any(ch in string.punctuation.replace("_", "") for ch in user_input):
    print(False)
elif " " in user_input:
    print(False)
elif "__" in user_input:
    print(False)
elif keyword.iskeyword(user_input):
    print(False)
else:
    print(True)
