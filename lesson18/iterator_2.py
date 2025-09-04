"""Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N."""


class EvenIterator:
    def __init__(self, n):
        self.x = -2
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= self.n:
            self.x += 2
            return self.x
        else:
            raise StopIteration


iterable = EvenIterator(11)
for i in iterable:
    print(i)
