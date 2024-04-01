list = [1,2,3,5,3, 6, 2, 1]

for i in list:
    if list.count(i) > 1:
        list.remove(i)


print (list)



list = [1,2,3,5,3, 6, 2, 1]
new_list = []

for i in list:
    if not i in new_list:
        new_list.append(i)

print (new_list)