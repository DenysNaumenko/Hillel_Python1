
#Homework 2.1
# user_input = input("Please enter a 4-digit integer number: ")
#
# number = int(user_input)
# print(number // 1000)
# print((number // 100) % 10)
# print((number // 10) % 10)
# print(type(number % 10))
#


# Homework 2.2
user_input = input("Please enter a 5-digit integer number: ")

number = int(user_input)

d1 = number % 10
d2 = (number // 10) % 10
d3 = (number // 100) % 10
d4 = (number // 1000) % 10
d5 = number // 10000

reversed_number = d1 * 10000 + d2 * 1000 + d3 * 100 + d4 * 10 + d5

print(reversed_number)
