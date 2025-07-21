# 7. Маємо ліст з цілими числами, потрібно сформувати словник де ключ це число з ліста,
# а значення це кількість повторень цього числа, потрібно вивести словник з топ 3 чисел по повторюваності
numbs = [12, 34, -67, 356, -678, 100, -678, 12, 356,-678, 0, 67,100, 32, 34, 100, -678]

numbs_as_key = []
quantity_as_value = []

for n in numbs:
    if n not in numbs_as_key:
        numbs_as_key.append(n)

for l in numbs_as_key:
    quantity_as_value.append(numbs.count(l))

numbs_dict = dict(zip(numbs_as_key,quantity_as_value))
print(numbs_dict)

sorted_values = sorted(numbs_dict.items(),key=lambda item:item[1], reverse=True )
print(sorted_values)
sorted_dict = dict(sorted_values[0:3])
print(sorted_dict)

