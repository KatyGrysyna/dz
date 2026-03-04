import string

text = input("Введіть дві літери через дефіс: ")
letters = string.ascii_letters

s, e = text.split("-")
s_in = letters.index(s)
e_in = letters.index(e)
result = letters[s_in:e_in + 1]

print(result)

