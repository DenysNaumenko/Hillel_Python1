while True:
    first_number = float(input("Введіть число: "))
    action = input("Введіть оператор(+, -, *, /): ")
    second_number = float(input("Введіть число: "))

    if action == "+":
        result = first_number + second_number
    elif action == "-":
        result = first_number - second_number
    elif action == "*":
        result = first_number * second_number
    elif action == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Помилка: На нуль ділити не можна"
    else:
        result = "Помилка: невідомий оператор!"

    if type(result) == float and result.is_integer():
        result = int(result)

    print("Результат:", result)

    action_confirm = input("Бажаєте продовжити?(yes/y, no/n): ").lower()
    if action_confirm not in ["yes", "y"]:
        print("The end")
        break
