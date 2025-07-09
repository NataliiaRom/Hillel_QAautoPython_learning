user_string = input("Enter any string here: ")

result_list = []
result_mark = []
for i in user_string:
    if i.isalpha() | i.isnumeric():
        i_count = user_string.count(i)
        info = f'Symbol "{i}" is met {i_count} times.'

        if info not in result_list:
            result_list.append(info)

            if i_count >=10:
                result_mark.append("True")
            else:
                result_mark.append("False")

result_dict = dict(zip(result_list, result_mark))

for j in result_dict.items():
    print(j)