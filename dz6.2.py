seconds_in = int(input("Введіть к-ть секунд (від 0 до 8639999):"))
if 0 <= seconds_in < 8640000:

    days, seconds_left = divmod(seconds_in, 86400)
    hours, seconds_left = divmod(seconds_left, 3600)
    minutes, seconds = divmod(seconds_left, 60)

    h = str(hours).zfill(2)
    m = str(minutes).zfill(2)
    s = str(seconds).zfill(2)

    if days % 10 == 1 and days % 100 != 11:
        word = "день"
    elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
        word = "дні"
    else:
        word = "днів"
    print(f"{days}{word}, {h}:{m}:{s}")
else:
    print("Помилка! Число повинно бути від 0 до 8639999")