import unittest
import sys
import pathlib

sys.path.insert(0,str(pathlib.Path(__file__).parent.parent.parent))

from lesson9.homeworks09 import top_3_symbols
from lesson9.homeworks09 import combined_dict
from lesson9.homeworks09 import top_3_list_of_numbs_met
from lesson9.homeworks09 import fixed_length_list
from lesson9.homeworks09 import tuple_of_unique_values

print("#####Tests for TASK1#####")
class Task1Tests(unittest.TestCase):
    def test_output_contains_3_lines(self):
        actual_len = len(top_3_symbols("abc"))
        expected_len = 3
        self.assertEqual(actual_len, expected_len, msg=f"The function should return {expected_len} lines, but it returned a different number.")
        print("Test passed: Output contains exactly 3 lines.")

    def test_input_is_not_empty(self):
        actual_input = top_3_symbols("ab")
        self.assertTrue(actual_input, msg = "The text is empty. Cannot get top 3 met letters.")
        print("Test passed: Input contains not empty text")

print("#####Tests for TASK2#####")
class Task2Tests(unittest.TestCase):
    def test_both_arguments_are_dictionaries(self):
        dict1 = {
            "o": 56,
            "a": 10,
            "b": 20,
            "c": 30,
            "d": 40,
            "e": 50
        }
        # dict2 = [123,345]
        dict2 = {
            "a": 5,
            "b": 15,
            "c": 25,
            "d": 35,
            "f": 45
        }

        actual_parameter1 = dict1
        actual_parameter2 = dict2
        expected_type = dict
        self.assertIsInstance(actual_parameter1,expected_type,
                              msg = f"The parameter 'dict1' type {type(actual_parameter1)} is wrong. Has to be 'dictionary'")
        self.assertIsInstance(actual_parameter2, expected_type,
                              msg=f"The parameter 'dict2' type {type(actual_parameter2)} is wrong. Has to be 'dictionary'")
        print(f"Test passed: The parameters type is {expected_type}")

    def test_dictionaries_have_int_values(self):
        dict1 = {
            "o": 56,
            "a": 678,
        }
        # dict2 = [123,345]
        dict2 = {
            "a": 567,
            "f": 56
        }
        expected_instance = int
        for i in dict1.values():
            self.assertIsInstance(i,expected_instance,msg = f"The value '{i}' type of 'dict1' {type(i)} is wrong. Has to be 'int'")
        for j in dict2.values():
            self.assertIsInstance(j,expected_instance,msg = f"The value '{j}' type of 'dict1' {type(j)} is wrong. Has to be 'int'")


print("#####Tests for TASK3#####")
class Task3Tests(unittest.TestCase):
    def test_check_is_number_is_met_more_than_once(self):
        list_of_numbs = [12, 34, -67, 356, -678, 100, -678, 12, 356, -678, 0, 67, 100, 32, 34, 100, -678]

        not_allowed_quantity = 1
        for t in top_3_list_of_numbs_met(list_of_numbs).values():
            self.assertGreater(t, not_allowed_quantity,
                                   msg=f"there are numbers, that are met only once. Each number should be met more that 1 times.")


    def test_check_output_has_only_ints(self):
        list_of_numbs = [12, 678, 67,80]
        allowed_instance = int
        for key in top_3_list_of_numbs_met(list_of_numbs).keys():
            # print(key)
            self.assertIsInstance(key,allowed_instance,
                                      msg = f"'{key}' type is not 'int'. Test failed.")

    def test_list_elements_are_immutable(self):
        list_of_numbs = [12, 678, "a", "a"]
        def is_mutable(obj):
            return isinstance(obj,(dict,set,list))
        for t in list_of_numbs:
            self.assertFalse(is_mutable(t),
                             msg = f"'{t}' is mutable. The test cannot be performed")

print("#####Tests for TASK4#####")
class Task4Tests(unittest.TestCase):
    def test_check_there_are_dashes_in_output(self):
        # list0 = ["abcde", "abcdefgh1234", "abcdef", "abcdefghtyui", "123"]
        list0 = ["abcde", "abcdefgh1234", "abcdef", "abcdefghtyui", "123"]
        dashes_count = 0
        for r in fixed_length_list(list0):
            if "_" in r:
                dashes_count += 1

        expected_result = 1
        if dashes_count == 0:
            self.assertGreaterEqual(dashes_count, expected_result,
                             msg = f"None of the element contains dashes. This means, all elements are of a same length. This is not allowed.")


print("#####Tests for TASK5#####")


class Task5Tests(unittest.TestCase):
    def test_tuple_has_more_than_one_element(self):
        list5 = [12,12,13]
        expected_length = 2
        actual_length = len(tuple_of_unique_values(list5))
        self.assertGreaterEqual(actual_length,expected_length)

    def test_tuple_length_is_less_than_5(self):
        list5 = [12, 45, 67, 56, 45, 12, 67]
        expected_length = 5
        actual_length = len(tuple_of_unique_values(list5))
        self.assertLessEqual (actual_length,expected_length)


if __name__ == ("__main__"):
    unittest.main()

