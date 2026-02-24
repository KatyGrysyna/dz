#lst = [0, 1, 0, 12, 3]
#lst = [0]
#lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
final = []

for lst1 in lst:
    if lst1 != 0:
        final.append(lst1)
for lst1 in lst:
    if lst1 == 0:
        final.append(lst1)
print(final)