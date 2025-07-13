def compare_grades(grades1, grades2):
    # YOUR CODE HERE
    comparison_dict = {}

    score_difference1_based_on_dict1 = []
    for k in grades1.keys():
        ####to uncomment the 'if' line, if we don't want unique users to be in a final list
        # if k in grades2.keys():
            diff = grades1.get(k) - grades2.get(k, 0)
            score_difference1_based_on_dict1.append(diff)
    comparison_dict.update(dict(zip(grades1.keys(), score_difference1_based_on_dict1)))

###to comment the below section until 'return', if we don't want unique users to be in a final list
    score_difference_based_on_dict2 = []
    list_of_unique_keys_of_dict2 = []
    for l in grades2.keys():
        if l not in grades1.keys():
            diff = grades1.get(l,0) - grades2.get(l)
            score_difference_based_on_dict2.append(diff)
            list_of_unique_keys_of_dict2.append(l)

    comparison_dict.update(dict(zip(list_of_unique_keys_of_dict2, score_difference_based_on_dict2)))


    return comparison_dict

    # return x


grades_1 = {'Анна Коваленко': 92, 'Олег Петров': 85, 'Ірина Сидорова': 78, 'Свирид Свиридович': 99}
grades_2 = {'Анна Коваленко': 92, 'Соломія Опришко': 48, 'Олег Петров': 87, 'Ірина Сидорова': 80}

result = compare_grades(grades_1, grades_2)
print(result)
