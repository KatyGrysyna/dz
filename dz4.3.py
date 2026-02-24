import random
#оптимальний варіант рішення
num = [random.randint(3, 100) for _ in range(random.randint(3, 10))]
res = [num[0], num[2], num[-2]]
print(num)
print(res)

