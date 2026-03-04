while True:
    x = int(input('Введіть перше число:'))
    y = int(input('Введіть друге число:'))
    z = input('Введіть дію над числами(+, -, *, /):')
    if z == "+":
        print(x + y)
    elif z == "-":
        print(x - y)
    elif z == "*":
        print(x * y)
    elif z == "/":
        if y == 0:
            print('Ділення на 0 неможливе')
        else:
            print(x / y)
    else:
        print('Невірна дія')
    answer = input("Продовжити роботу? (y/n):").lower()

    if answer != "y":
        print("Роботу завершено")
        break



