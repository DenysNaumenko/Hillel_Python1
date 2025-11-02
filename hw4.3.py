import random

for i in range(3):
    my_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]

    indices_to_select = [0, 2, -2]

    if len(my_list) >= 3:
        new_list = [my_list[i] for i in indices_to_select]
        print(f"{my_list} == {new_list}")
