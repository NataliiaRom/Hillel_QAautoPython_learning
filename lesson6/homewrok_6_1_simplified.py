user_string = input("Enter any string here: ")
check_value = 10

unique_symbols = []
symbols_count = []
for i in user_string:
    if i != " " and i not in unique_symbols:
        unique_symbols.append(i)
        count_i = user_string.count(i)
        symbols_count.append(count_i)

found = False
for j in symbols_count:
    if j >= check_value:
        found = True
        print(True)
        break

if not found:
    print(False)

