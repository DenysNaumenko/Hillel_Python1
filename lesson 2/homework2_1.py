user_input = input("Please enter a 4-digit integer number: ")

number = int(user_input)
print(number // 1000)
print((number // 100) % 10)
print((number // 10) % 10)
print(number % 10)
