# lst = [0, 1, 7, 2, 4, 8]
lst = [1, 3, 5]
# lst = [6]
# lst = []


total_sum = 0

for i, element in enumerate(lst):
    if i % 2 == 0:
        total_sum += element

if lst:
    last_element = lst[-1]
    result = total_sum * last_element
    print(result)
else:
    print(0)
