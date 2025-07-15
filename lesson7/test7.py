# words = ['hi','hola','wwwwrrr','привіт','hallo', 'bonjour', '1234567']
# for index,value in enumerate(words):
#     print(index,value)

# 7. Маємо ліст з цілими числами, потрібно сформувати словник де ключ це число з ліста,
# а значення це кількість повторень цього числа, потрібно вивести словник з топ 3 чисел по повторюваності
numbs = [12, 34, -67, 356, -678, 100, 12, 356, 0, 67, 32, 34]

numbs_unique = []
for i in numbs:
    if i not in numbs_unique:
        numbs_unique.append(i)
print(numbs_unique)

numbs_unique_to_store_met_items = numbs_unique

count_numbs_unique = []

for j in numbs_unique:
    for index, value in enumerate(numbs):
        if value == j:
            print(str(value).count())
# for j in numbs_unique_to_store_met_items:
#     count = 0
#     if j in numbs:
#         count +=1
#         count_numbs_unique.append(count)
#         numbs_unique_to_store_met_items.remove(j)
#     count_numbs_unique.append(count)

print(count_numbs_unique)
