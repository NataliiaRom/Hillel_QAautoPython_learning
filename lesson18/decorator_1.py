"""Напишіть декоратор, який логує аргументи та результати викликаної функції."""

import logging

logger = logging.getLogger("log_decorator")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def log_decorator(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        logger.info(f"You have passed the following arguments to you function: {args}, {kwargs}")
        logger.info(f"The result of your fucntion execution is: {result}")
        return result
    return wrapper

@log_decorator
def my_func(name, age):
    return f"I am {name}, I am {age} years old"

print(my_func('Nata',age = 36))