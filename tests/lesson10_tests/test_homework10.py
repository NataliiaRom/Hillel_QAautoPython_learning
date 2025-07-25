import pytest

from lesson10.homeworks10 import top_3_symbols
from lesson10.homeworks10 import combined_dict
from lesson10.homeworks10 import top_3_list_of_numbs_met
from lesson10.homeworks10 import fixed_length_list
from lesson10.homeworks10 import tuple_of_unique_values

print("#####Tests for TASK1#####")

class TestTask1:

    def test_TypeError_raised_if_input_not_string(self):
        test_input = 123
        with pytest.raises(TypeError) as te:
            top_3_symbols(test_input)
        assert str(te.value) == "The input type must be 'str' only"

    def test_input_value_not_empty(self):
        test_input = ""
        with pytest.raises(ValueError) as ve:
            top_3_symbols(test_input)
        assert str(ve.value) == "The string cannot be empty"

print("#####Tests for TASK2#####")

def test_dicts_have_only_int_values():
    test_dict1 = {"a":234}
    test_dict2 = {"b":123}
    with pytest.raises(ValueError):
        combined_dict(test_dict1,test_dict2)


print("#####Tests for TASK3#####")

def test_output_dict_values_count_less_than10():
    list_of_numbs = [12, 12, 12, 12, -678, 100, -678, 12, 356, -678, 0, 67, 100, 32, 34, 100, -678]
    result_dict = top_3_list_of_numbs_met(list_of_numbs)
    assert sum(result_dict.values()) <=10, \
        f"{sum(result_dict.values())} is greater than 10. You cannot proceed."

print("#####Tests for TASK4#####")

def test_ValueError_is_raised_if_output_list_elements_of_same_size():
    test_list = ["asd", "fgh", "gvv"]
    with pytest.raises(ValueError):
        fixed_length_list(test_list)


print("#####Tests for TASK5#####")

def test_1st_elt_less_than50_and_last_elt_bigger_than15():
    list5 = [12, 45, 67, 56, 45, 23, 98, 12, 67]
    final_list = tuple_of_unique_values(list5)
    assert final_list[0] <=50 and final_list[-1]>=15, \
        f"The border values '{final_list[0]}' and '{final_list[-1]}' are not appropriate to proceed.]"


