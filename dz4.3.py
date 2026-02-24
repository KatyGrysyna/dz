import random

num = []
for i in range(random.randint(3, 10)):
    num.append(random.randint(1, 100))
res = [num[0], num[2], num[-2]]
print(num)
print(res)

