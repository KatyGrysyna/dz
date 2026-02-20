x = int(input('Введіть перше число:'))
y = int(input('Введіть друге число:'))
z = input('Введіть дію над числами(+, -, *, /):')
if z == "+":
    print(x + y)
if z == "-":
    print(x + y)
if z == "*":
    print(x * y)
if z == "/":
    if y == 0:
        print('Ділення на 0 неможливе')
    else:
        print(x / y)