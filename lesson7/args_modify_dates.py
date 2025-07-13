#########Version1 ############

# def solution(*args, sep="."):
#     # YOUR CODE HERE
#     date = ""
#     for arg in args:
#         # print(arg)
#         date += f"{arg}{sep}"
#
#     date = date[:-1]
#     return date
#
# print(solution('01','11','1987'))
# print(solution('01','11','1987', sep = "/"))

#########Version2############
def solution(*args, sep="."):
    # YOUR CODE HERE
    dates = []
    for arg in args:
        date_list = []
        d,m,y = arg
        date_list.append(str(d))
        date_list.append(str(m))
        date_list.append(str(y))

        date_str = sep.join(date_list)
        dates.append(date_str)

    return dates


print(solution([11, 22, 2003], ['05', 12, 2003], sep = '/'))

