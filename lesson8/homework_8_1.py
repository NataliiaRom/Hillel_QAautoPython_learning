list1 = ["1, 2, 3, 4", "1, 2, 3, 4, 50", "1, 2, 3a"]


def list_elts_sum(list):
    suma = []
    for i in list:
        i_str_as_list = i.split(',')
        i_list_of_ints = []
        try:
            for j in i_str_as_list:
                i_list_of_ints.append(int(j.strip()))
            suma.append(sum(i_list_of_ints))
        except Exception as esc:
            suma.append(f"{type(esc).__name__}: Cannot do this")

    return suma

print(list_elts_sum(list1))