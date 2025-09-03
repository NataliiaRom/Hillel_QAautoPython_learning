"""Напишіть генератор, який повертає послідовність парних чисел від 0 до N."""


def even_numb_gen(n: int):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


n = 10
# option 1
for num in even_numb_gen(n):
    print(num)

# option 2
print(list(even_numb_gen(n)))

# option 3
gen = even_numb_gen(n)

while True:
    try:
        print(next(gen))
    except StopIteration as si:
        print(repr(si))
        break

print("hello")
