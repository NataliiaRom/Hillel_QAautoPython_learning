lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

string_list = []
for i in lst1:

##### Version with isinstance() #######
    if isinstance(i, str):
        string_list.append(i)

##### Version with .__name__ #######
    # if type(i).__name__ == 'str':
    #     string_list.append(i)
    else:
        continue

print(string_list)
