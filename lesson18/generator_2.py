"""Створіть генератор, який генерує послідовність Фібоначчі до певного числа N."""

# тут не підглядала в теорію з готовим прикладом, писала сама, але згодна,
# що приклад в теорії красивіше реалізований

def fibo(n):
    a, b = 1, 1
    yield a
    yield b
    while (a + b) <= n:
        c = a + b
        yield c
        a, b = b, c


# 1
fibon = list(fibo(40))
print(fibon)

# 2
fibon = fibo(40)
while True:
    try:
        print(next(fibon))
    except StopIteration:
        break

# 3
fibon1 = fibo(40)
for i in fibon1:
    print(i)
