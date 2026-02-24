lst = [1, 3, 5]
#lst = [6]
#lst = []

if len(lst) == 0:
    res = 0
else:
    final = 0
    for i in range(0, len(lst), 2):
        final = final + lst[i]
    res = final * lst[-1]
print(res)