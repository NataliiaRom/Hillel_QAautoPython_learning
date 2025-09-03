"""Реалізуйте ітератор для зворотного виведення елементів списку."""

class ReverseRemoveIterator:
    def __init__(self,my_list:list):
        self.my_list = my_list

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.my_list) == 0:
            raise StopIteration
        else:
            self.my_list.pop()

        return self.my_list

my_list = [1,2,3,4,5,6]
iterable = ReverseRemoveIterator(my_list)
for l in iterable:
    print(l)