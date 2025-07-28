# I. Маємо рядок, потрібно вивести 3 символа що найчастіше зустрічаються в тесті і кількість входжень,
#  пробіли ігноруються
print("TASK1")
print("_"*40)
def top_3_symbols(text):

    count_set = set()
    for i in text:
        if i.isalpha():
            symbol_count = text.lower().count(i)

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

    # print(f'The sorted list of the met symbols:\n' + "*" * 10)
    # for k in sorted_by_number_count_list:
    #     print(f'{k}')
    # print("*" * 10)
    # print("Top 3 letters met:\n")

    list_of_top3_met_letters = sorted_by_number_count_list[0:3]
    # for j in (sorted_by_number_count_list[0:3]):
    #     print(j)
    return list_of_top3_met_letters


text1 = "Welcome to the Dummy Text Generator!\
This handy tool helps you create dummy text for all your layout needs.\
We are gradually adding new functionality and we welcome your suggestions and feedback.\
Please feel free to send us any additional dummy texts."

print(top_3_symbols(text1))


# II. Маємо два словники, в цих словниках є однакові ключі, значення - цілі числа.
#  Потрібно сформувати третій словник, в якому при повторюваних ключах в новий переноситься лише більше значення,
#  якщо якийсь ключ унікальний він просто переноситься в новий словник
print("_"*40)
print("TASK2")
print("_"*40)

def combined_dict(dict1,dict2):

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

    return dict3

dict01 = {
    "o": 56,
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50
}

dict02 = {
    "a": 5,
    "b": 15,
    "c": 25,
    "d": 35,
    "f": 45
}

print(combined_dict(dict01,dict02))


# III. Маємо ліст з цілими числами, потрібно сформувати словник де ключ це число з ліста,
# а значення це кількість повторень цього числа, потрібно вивести словник з топ 3 чисел по повторюваності
print("_"*40)
print("TASK3")
print("_"*40)

def top_3_list_of_numbs_met(list_of_numbs):

    list_of_numbs_as_key = []
    quantity_as_value = []

    for n in list_of_numbs:
        if n not in list_of_numbs_as_key:
            list_of_numbs_as_key.append(n)

    for l in list_of_numbs_as_key:
        quantity_as_value.append(list_of_numbs.count(l))

    list_of_numbs_dict = dict(zip(list_of_numbs_as_key,quantity_as_value))
    # print(list_of_numbs_dict)

    sorted_values = sorted(list_of_numbs_dict.items(),key=lambda item:item[1], reverse=True )
    # print(sorted_values)
    sorted_dict = dict(sorted_values[0:3])
    return sorted_dict

list_of_numbs = [12, 34, -67, 356, -678, 100, -678, 12, 356,-678, 0, 67,100, 32, 34, 100, -678]
print(top_3_list_of_numbs_met(list_of_numbs))


# IV. Маємо ліст рядків різної довжини, потрібно сформувати новий ліст рядків фіксованої довжини з попередніх рядків,
#  довжина дорівнює довжині найдовшого рядка, ті рядки що коротші за найдовший рядок повинні бути доповнені нижніми
#  підкресленнями
print("_"*40)
print("TASK4")
print("_"*40)

def fixed_length_list(list):

    list_new = []

    longest_elt = 0
    for k in range(len(list)):
        if len(list[k]) >= len(list[longest_elt]):
            longest_elt = k

    for l in list:
        if len(l) < len(list[longest_elt]):
            diff = len(list[longest_elt]) - len(l)
            new_elt = "_"*diff + l
            list_new.append(new_elt)
        else:
            list_new.append(l)

    return list_new

list4 = ["abcde", "abcdefgh1234", "abcdef", "abcdefghtyui", "123"]
print(fixed_length_list(list4))

# V. Маємо список цілих чисел, потрібно на виході отримати тупл унікальних значень цього списку у зворотньому напрямку
print("_"*40)
print("TASK5")
print("_"*40)

def tuple_of_unique_values(list):

    list_reverse = list[::-1]
    list_reverse_without_dups = []

    for i in range(len(list_reverse)):
        if list_reverse[i] not in list_reverse_without_dups:
            list_reverse_without_dups.append(list_reverse[i])

    tuple_reverse_without_dups = tuple(list_reverse_without_dups)
    return tuple_reverse_without_dups

list5 = [12, 45, 67, 56, 45, 23, 98, 12, 67]
print(tuple_of_unique_values(list5))

