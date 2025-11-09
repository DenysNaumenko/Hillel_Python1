import string

letters = string.ascii_lowercase + string.ascii_uppercase

user_input = input("Введіть дві літери через дефіс: ")
start, end = user_input.split('-')

start_index = letters.index(start)
end_index = letters.index(end)

if start_index <= end_index:
    result = letters[start_index:end_index + 1]
else:

    result = letters[start_index:] + letters[:end_index + 1]

print(''.join(result))
