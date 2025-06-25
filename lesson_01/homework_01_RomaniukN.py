# task 01 == Виправте синтаксичні помилки
print("TASK1", end = '\n######\n')

print("Hello")
print("world!", end = '\n\n')

# task 02 == Виправте синтаксичні помилки
print("TASK2", end = '\n######\n')

hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!\n")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("TASK3", end = '\n######\n')

for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
print("TASK4", end = '\n######\n')

apples = 2
bananas = apples * 4
print(f'There are {apples} apples and {bananas} bananas\n')


# task 05 == виправте назви змінних
print("TASK5", end = '\n######\n')

_1_storona = 1
_storona_2 = 2
сторона_3 = 3
storona_4_ = 4
print(f'There figure sides have the following measurements: {_1_storona}cm, {_storona_2}cm, {сторона_3}cm, '
      f'{storona_4_}cm \n')

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print("TASK6", end = '\n######\n')

perimeter = _1_storona + _storona_2 + сторона_3 + storona_4_
print(perimeter, end = '\n\n')


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print("TASK7", end = '\n######\n')

apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
trees_total = apple_trees + pear_trees + plum_trees
print(f'The total amount of the planted in the garden trees is: {trees_total}\n')
# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print("TASK8", end = '\n######\n')
morning_temp = 5
afternoon_temp = morning_temp - 10
evening_temp = afternoon_temp + 4
print(f'The evening temperature is {evening_temp}°C\n')

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print("TASK9", end = '\n######\n')

total_boys = 24
total_girls = total_boys / 2
ill_boy = 1
absent_girls = 2
total_kids = total_boys + total_girls
absent_kids = ill_boy + absent_girls
present_kids = int(total_kids - absent_kids)

print(f'Today there are {present_kids} kids present at the theater class.\n')
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print("TASK10", end = '\n######\n')

book1_cost = 8
book2_cost = book1_cost + 2
book3_cost = (book1_cost + book2_cost) / 2
total_cost = book1_cost + book2_cost + book3_cost

print(f'To buy all 3 books you should pay {total_cost:.2f} UAH.\n')
