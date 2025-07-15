# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 0
    # Complete the while loop condition.
    while result <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
print('#####TASK1#####')
multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print('#####TASK2#####')

def suma(x,y):
    result = x+y

    return result

print(suma(56,-54))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print('#####TASK3#####')
def math_avg(list):
    list_length = len(list)
    list_sum = sum(list)

    avg = list_sum/list_length
    return f"{avg:.2f}"

list_1 = [23,45,6,9,0,87]
print(math_avg(list_1))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print('#####TASK4#####')
def reverse_str(str):
    str_rev = str[::-1]
    return str_rev

string_1 = 'abcdefg123'
print(reverse_str(string_1))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print('#####TASK5#####')

def largest_word(list):
    length_list = []

    for i in range(0,len(list)):
        length = len(list[i])
        length_list.append(length)

    max_value_in_length_list = max(length_list)

    largest_words = []
    for index,value in enumerate(length_list):
        if value == max_value_in_length_list:
            largest_words.append(list[index])

    # print(length_list)
    return largest_words

words = ['hi','hola','wwwwrrr1','привіт','hallo', 'bonjour0', '12345678']
print(largest_word(words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print('#####TASK6#####')
def find_substring(str1, str2):
    if str2 in str1:
        find_str2_index = str1.find(str2)
        return find_str2_index
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
""" 
Маємо рядок, потрібно зробити так щоб всі символи в рядку чередувалися - велика, маленька, пробіли не впливають
на чередування, але виводяться в фінальному тексті
"""
print('#####TASK7#####')
def bigsmall_ignorespace(string):
    space_indexes = []
    for s in range(len(string)):
        if string[s] == " ":
            space_indexes.append(s)

    string_without_spaces = string.replace(" ", "")
    string_modified = ""

    for c in range(len(string_without_spaces)):
        if string_without_spaces[c].isalpha() and c % 2 == 0:
            string_modified += string_without_spaces[c].upper()
        else:
            string_modified += string_without_spaces[c].lower()
    # print(string_modified)

    string_modified_list = list(string_modified)
    for b in space_indexes:
        string_modified_list.insert(b, " ")

    modified_string = ''.join(string_modified_list)
    return modified_string

string3 = (f"Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
           f"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
           f"when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
           f"It has survived not only five centuries, but also the leap into electronic typesetting, "
           f"remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset "
           f"sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like "
           f"Aldus PageMaker including versions of Lorem Ipsum.\n")

print(bigsmall_ignorespace(string3))

# task 8
"""
Маємо список цілих чисел, потрібно на виході отримати тупл унікальних значень цього списку у зворотньому напрямку
"""
print('#####TASK8#####')
def reverse_unique_tuple(list):

    list_reverse = list[::-1]
    list_reverse_without_dups = []

    for i in range(len(list_reverse)):
        if list_reverse[i] not in list_reverse_without_dups:
            list_reverse_without_dups.append(list_reverse[i])

    tuple_reverse_without_dups = tuple(list_reverse_without_dups)
    return tuple_reverse_without_dups

list01 = [12, 45, 67, 56, 45, 23, 98, 12, 67]
print(reverse_unique_tuple(list01))

# task 9
"""
Маємо рядок, потрібно видалити весь текст що знаходиться всередині дужок () і самі дужки, результат вивести
"""
print('#####TASK9#####')
def remove_brackets(string):
    bracket_open_index_list = []
    bracket_close_index_list = []
    start_index_open = 0
    start_index_close = 0

    for i in range(len(string)):
        if string[i] == "(":
            bracket_open_index_list.append(i)
        elif string[i] == ")":
            bracket_close_index_list.append(i)

    # print(bracket_open_index_list, bracket_close_index_list)

    with_brackets_string_list = []
    for k, l in zip(bracket_open_index_list, bracket_close_index_list):
        with_brackets_string = string[k:(l + 1)]
        with_brackets_string_list.append(with_brackets_string)

    # print(with_brackets_string_list)

    for u in with_brackets_string_list:
        string = string.replace(u, "")

    return string

string2 = (f"Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
           f"(Lorem Ipsum has been the industry's standard) dummy text ever (since the 1500s, "
           f"when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
           f"It has survived not only five centuries,) but also (the leap into electronic typesetting, "
           f"remaining essentially unchanged. It was popularised in the) 1960s xaxaxa (with the release of Letraset "
           f"sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like "
           f"Aldus PageMaker including versions of Lorem Ipsum.)\n")

print(remove_brackets(string2))
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
print('#####TASK10#####')
"""
 Маємо ліст чисел, потрібно розбити його на два ліста: парні і не парні,
і вивести спочатку один без ком, з пробілами між числами, а потім інший, так само без ком, з пробілами
"""

def make_2_lists(list):
    odd_numbers = []
    even_numbers = []

    for n in list:
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

numbers = [2, 3, 56, 78, 9, 65, -40, 13, -75]

make_2_lists(numbers)

