#lst = [12, 3, 4, 10]
#lst = [1]
#lst = []
#lst = [12, 3, 4, 10, 8]

if len(lst) >1:
    last = lst[-1]
    lst1 = lst[:-1]
    lst = [last] + lst1
print(lst)

