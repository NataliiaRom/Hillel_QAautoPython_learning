alice_in_wonderland = '''

"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don\'t much care where ——" said Alice.\n
"Then it doesn\'t matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."

'''

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print("TASKs 01-03", end = '\n######')
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("TASK 04", end = '\n######\n')
black_sea_square = 436402
azov_sea_square = 37800
common_square = black_sea_square + azov_sea_square
print(f'The total square, both Black and Azov seas occupy equals {common_square} km2\n')
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("TASK 05", end = '\n######\n')
total_items = 375291
storage_1_2_items = 250449
storage_2_3_items = 222950
storage3_items = total_items - storage_1_2_items
storage2_items = storage_2_3_items - storage3_items
storage1_items = total_items - storage_2_3_items

print(f'There are\n'
      f'\t{storage1_items:,} items at Storage1,\n'
      f'\t{storage2_items:,} items at Storage2 and\n'
      f'\t{storage3_items:,} items at Storage3.\n' )

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("TASK 06", end = '\n######\n')

duration = 18 # months
partial_payment = 1179 # UAH per month
pc_price = duration * partial_payment
print(f'The total price of the PC equals {pc_price:,} UAH.\n')


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("TASK 07", end = '\n######\n')
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f'The division remainer\n'
      f'\tof \'8019 : 8\' is {a}\n'
      f'\tof \'9907 : 9\' is {b}\n'
      f'\tof \'2789 : 5\' is {c}\n'
      f'\tof  \'7248 : 6\' is {d}\n'
      f'\tof \'7128 : 5\' is {e}\n'
      f'\tof \'19224 : 9\' is {f}.\n')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("TASK 08", end = '\n######\n')
big_pizza = 4
big_pizza_price = 274
big_pizza_total = big_pizza * big_pizza_price

small_pizza = 2
small_pizza_price = 218
small_pizza_total = small_pizza * small_pizza_price

juice = 4
juice_price = 35
juice_total = juice * juice_price

cake = 1
cake_price = 350
cake_total = cake * cake_price

water = 3
water_price = 21
water_total = water * water_price

total_price = big_pizza_total + small_pizza_total + juice_total + cake_total + water_total
print(f'Irynka should spend {total_price} UAH for her birthday order.\n')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("TASK 09", end = '\n######\n')

photos_total = 232
photos_per_page = 8

if (photos_total % photos_per_page == 0):
    pages_to_use = int(photos_total / photos_per_page)
else:
    pages_to_use = int(photos_total / photos_per_page + 1)

print(f'To stick all the photos Igor will use {pages_to_use} pages in his album.\n')
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print("TASK 10", end = '\n######\n')
distance = 1600  # km
interval = 100  # km
petrol_per_interval = 9  # liter per interval
car_tank_capacity = 48  # liter

petrol_total = (distance / interval) * petrol_per_interval

if (petrol_total % car_tank_capacity == 0):
    tank_station_stops = int(petrol_total / car_tank_capacity)
else:
    tank_station_stops = int(petrol_total / car_tank_capacity) + 1


print(f'To perform the trip from Kharkiv to Budapest the family should spend {petrol_total:.2f} liters of petrol.\n'
      f'That\'s why they would need to tank their auto {tank_station_stops} times.')
