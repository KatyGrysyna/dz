import random

lst = random.randint(3,10)
num = []
for i in range(lst):
    num.append(random.randint(0, 100))
final = [num[0], num[2], num[-2]]
print(num)
print(final)

