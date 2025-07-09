numb_list = [56, 87, 90, -89, -44, 100, 13, 133]

even_list = []
for i in numb_list:
    if i % 2 == 0:
        even_list.append(i)
    # else:
    #     continue
print(sum(even_list))
print(even_list)
