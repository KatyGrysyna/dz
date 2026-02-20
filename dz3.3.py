lst = [1, 2, 3, 4, 5, 6]
#lst = [1, 2, 3]
#lst = [1, 2, 3, 4, 5]
#lst = [1]
#lst = []
n = len(lst)
print(n)
if n == 0:
    res = [[], []]
elif n % 2 == 0:
    half = n // 2
    res = [lst[:half], lst[half:]]
else:
    half = n // 2 + 1
    res = [lst[:half], lst[half:]]

print(res)