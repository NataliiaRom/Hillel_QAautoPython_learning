list1 = ["1, 2, s3, 4", "1, 2, 3, 4, 50", "1, 2a, 3"]


def list_elts_sum(list):
    suma = []
    for i in list:
        i_str_as_list = i.split(',')
        i_list_of_ints = []
        for j in i_str_as_list:
            try:
                i_list_of_ints.append(int(j.strip()))
            except ValueError as ve:
                i_list_of_ints.append(None)
                break
        try:
            suma.append(sum(i_list_of_ints))
        except TypeError as te:
            suma.append(f"{type(te).__name__}: Cannot do this")

    return suma

print(list_elts_sum(list1))
