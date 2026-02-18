minutes = int(input('Введіть к-ть хвилин:'))
hours, mmin  = divmod(minutes, 60)
print(hours, 'годин', mmin, 'хвилин' )