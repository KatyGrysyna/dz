import string
import keyword

name = input("Введіть ім'я змінної:")
is_valid = True

if name in keyword.kwlist:
    is_valid = False
elif name[0].isdigit():
    is_valid = False
elif name != name.lower():
    is_valid = False
else:
    f = string.punctuation.replace("_","") + " "
    for char in name:
        if char in f:
            is_valid = False
if name.count("_") > 1 and name.strip("_") == "":
    is_valid = False
print(is_valid)

