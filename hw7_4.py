def common_elements():
    list_3 = [i for i in range(100) if i % 3 == 0]
    list_5 = [i for i in range(100) if i % 5 == 0]

    set_3 = set(list_3)
    set_5 = set(list_5)

    return set_3.intersection(set_5)


result = common_elements()
print(result)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
