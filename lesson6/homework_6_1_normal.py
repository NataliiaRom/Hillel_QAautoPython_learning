user_string = input("Enter any string here: ")
check_value = 10

unique_symbols = ""
for i in user_string:
    if i not in unique_symbols:
        unique_symbols += i

count_unique_symbols = len(unique_symbols)
if count_unique_symbols >= check_value:
    print(True)
else:
    print(False)