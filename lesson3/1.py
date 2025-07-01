# x = 345
# hun = x // 100
# ten = (x - hun*100) // 10
# one = (x - hun*100 - ten*10) // 1
# new_x = one * 100 + ten * 10 + hun * 1
#
# print(new_x)

x = 345
hun = x // 100
ten = (x // 10) % 10
one = x % 10
new_x = one * 100 + ten * 10 + hun * 1

print(hun,ten,one)