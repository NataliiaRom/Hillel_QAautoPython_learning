# 1. Маємо ліст чисел, потрібно розбити його на два ліста: парні і не парні,
#  і вивести спочатку один без ком, з пробілами між числами, а потім інший, так само без ком, з пробілами
numbers = [2, 3, 56, 78, 9, 65, -40, 13, -75]

odd_numbers = []
even_numbers = []

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(str(n))
    else:
        odd_numbers.append(str(n))
print(f'The initial list {numbers} is divided into 2 lists with odd and even numbers:'
      f'\n\n\t{even_numbers}, {odd_numbers}\n')

str_even_numbers = ' '.join(even_numbers)
str_odd_numbers = ' '.join(odd_numbers)
print(f'The even numbers are: {str_even_numbers}\n'
      f'The odd numbers are: {str_odd_numbers}\n')

# 2. Маємо рядок, потрібно визначити індекси першого і останнього входження символу в рядок,
#  вивести тупл з індексами,якщо входжень немає вивести (None, None)
string1 = (f"Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
           f"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
           f"when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
           f"It has survived not only five centuries, but also the leap into electronic typesetting, "
           f"remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset "
           f"sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like "
           f"Aldus PageMaker including versions of Lorem Ipsum.\n")
print(string1)


def first_last_index_of_symbol(search_str):
    first_index = string1.lower().strip().find(search_str)
    reverse_string = string1[::-1]
    last_index = len(string1) - reverse_string.lower().strip().find(search_str)

    if first_index != -1:
        return (first_index, last_index)
    else:
        return (None, None)


search_string = "mhg"
search_string_first_last_indexes = first_last_index_of_symbol(search_string)
print(f'The search string "{search_string}" first and last indexes are: {search_string_first_last_indexes}\n')

# 3. Маємо рядок, потрібно вивести 3 символа що найчастіше зустрічаються в тесті і кількість входжень,
#  пробіли ігноруються

count_set = set()
for i in string1:
    if i.isalpha():
        symbol_count = string1.lower().count(i)

        if symbol_count < 10:
            info_string = f'"{i}" is met 0{symbol_count} time(s).'
        else:
            info_string = f'"{i}" is met {symbol_count} time(s).'

        count_set.add(info_string)

count_list = []
for i in count_set:
    i_list = i.split(" ")
    count_list.append(i_list)

sorted_by_number_count_list = sorted(count_list, key=lambda item: item[3], reverse=True)

print(f'The sorted list of the met symbols:\n' + "*" * 10)
for k in sorted_by_number_count_list:
    print(f'{k}')
print("*" * 10 + "\nTop 3 letters met:\n")

for j in (sorted_by_number_count_list[0:3]):
    print(j)
print("*" * 10)

# 4. Маємо рядок, потрібно видалити весь текст що знаходиться всередині дужок () і самі дужки, результат вивести
string2 = (f"Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
           f"(Lorem Ipsum has been the industry's standard) dummy text ever (since the 1500s, "
           f"when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
           f"It has survived not only five centuries,) but also (the leap into electronic typesetting, "
           f"remaining essentially unchanged. It was popularised in the) 1960s xaxaxa (with the release of Letraset "
           f"sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like "
           f"Aldus PageMaker including versions of Lorem Ipsum.)\n")

bracket_open_index_list = []
bracket_close_index_list = []
start_index_open = 0
start_index_close = 0

for i in range(len(string2)):
    if string2[i] == "(":
        bracket_open_index_list.append(i)
    elif string2[i] == ")":
        bracket_close_index_list.append(i)

print(bracket_open_index_list, bracket_close_index_list)

with_brackets_string_list = []
for k, l in zip(bracket_open_index_list, bracket_close_index_list):
    with_brackets_string = string2[k:(l + 1)]
    with_brackets_string_list.append(with_brackets_string)

# print(with_brackets_string_list)

for u in with_brackets_string_list:
    string2 = string2.replace(u, "")

print(string2)

# 5. Маємо рядок, потрібно зробити так щоб всі символи в рядку чередувалися - велика, маленька, пробіли не впливають
#  на чередування, але виводяться в фінальному тексті

string3 = (f"Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
           f"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
           f"when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
           f"It has survived not only five centuries, but also the leap into electronic typesetting, "
           f"remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset "
           f"sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like "
           f"Aldus PageMaker including versions of Lorem Ipsum.\n")
space_indexes = []
for s in range(len(string3)):
    if string3[s] == " ":
        space_indexes.append(s)

string3_without_spaces = string3.replace(" ", "")
string3_modified = ""

for c in range(len(string3_without_spaces)):
    if string3_without_spaces[c].isalpha() and c % 2 == 0:
        string3_modified += string3_without_spaces[c].upper()
    else:
        string3_modified += string3_without_spaces[c].lower()
print(string3_modified)

string3_modified_list = list(string3_modified)
for b in space_indexes:
    string3_modified_list.insert(b, " ")

modified_string = ''.join(string3_modified_list)
print(modified_string)

# 6. Маємо два словники, в цих словниках є однакові ключі, значення - цілі числа.
#  Потрібно сформувати третій словник, в якому при повторюваних ключах в новий переноситься лише більше значення,
#  якщо якийсь ключ унікальний він просто переноситься в новий словник

dict1 = {
    "o": 56,
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50
}

dict2 = {
    "a": 5,
    "b": 15,
    "c": 25,
    "d": 35,
    "f": 45
}

dict3 = {}

dict3_keys = []
dict3_values = []
for k in dict1.keys():
    dict3_keys.append(k)
    if k not in dict2.keys():
        dict3_values.append(dict1.get(k))
    elif dict1.get(k) >= dict2.get(k, 0):
        dict3_values.append(dict1.get(k))
    else:
        dict3_values.append(dict2.get(k))

for l in dict2.keys():
    if l not in dict1.keys():
        dict3_keys.append(l)
        dict3_values.append(dict2.get(l))

dict3 = dict(zip(dict3_keys,dict3_values))

print(dict3)



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

# 8. Маємо ліст рядків різної довжини, потрібно сформувати новий ліст рядків фіксованої довжини з попередніх рядків,
#  довжина дорівнює довжині найдовшого рядка, ті рядки що коротші за найдовший рядок повинні бути доповнені нижніми
#  підкресленнями

list4 = ["abcde", "abcdefgh1234", "abcdef", "abcdefghtyui", "123"]
list4_new = []

longest_elt = 0
for k in range(len(list4)):
    if len(list4[k]) >= len(list4[longest_elt]):
        longest_elt = k

for l in list4:
    if len(l) < len(list4[longest_elt]):
        diff = len(list4[longest_elt]) - len(l)
        new_elt = "_"*diff + l
        list4_new.append(new_elt)
    else:
        list4_new.append(l)

print(list4_new)

# 9. Маємо список цілих чисел, потрібно на виході отримати тупл унікальних значень цього списку у зворотньому напрямку
list = [12, 45, 67, 56, 45, 23, 98, 12, 67]
list_reverse = list[::-1]
list_reverse_without_dups = []

for i in range(len(list_reverse)):
    if list_reverse[i] not in list_reverse_without_dups:
        list_reverse_without_dups.append(list_reverse[i])

tuple_reverse_without_dups = tuple(list_reverse_without_dups)
print(tuple_reverse_without_dups)
