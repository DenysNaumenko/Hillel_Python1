user_input = input("Введіть кількість секунд (0–8640000): ")

if not user_input.isdigit():
    print("Потрібно ввести число!")
else:
    seconds = int(user_input)

    if 0 <= seconds < 8640000:
        days = seconds // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        if days % 10 == 1 and days % 100 != 11:
            day_word = "день"
        elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
            day_word = "дні"
        else:
            day_word = "днів"

        print(f"{days} {day_word}, {hours:02d}:{minutes:02d}:{secs:02d}")
    else:
        print("Число має бути від 0 до 8640000!")
