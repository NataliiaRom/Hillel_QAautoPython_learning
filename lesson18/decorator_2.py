"""Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції."""


def exceptions_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            x = func(*args, **kwargs)
            return x
        except Exception as exc:
            return repr(exc)

    return wrapper


# 1
@exceptions_decorator
def division_by_zero(a, b):
    result = a / b
    return result


print(division_by_zero(5, 8))
print(division_by_zero(5, 0))
print(division_by_zero(5, 9))


# 2
def gen_value(n):
    for i in range(n):
        yield i


gen1 = gen_value(10)


@exceptions_decorator
def check_gen_value():
    while True:
        value = next(gen1)
        print(value)


print(check_gen_value())
