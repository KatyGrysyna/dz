number = input("Введіть ціле число:")
while int(number) > 9:
    n = 1
    for digit in number:
        n = n * int(digit)
    number = str(n)
print(int(number))