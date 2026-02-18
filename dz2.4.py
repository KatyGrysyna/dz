price = int(input('Введіть ціну:'))
discount = int(input('Введіть знижку(%):'))
final = price - ((discount / 100) * price)
print('Ціна зі знижкою:', final)