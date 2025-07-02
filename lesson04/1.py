# x = 345
# hun = x // 100
# ten = (x - hun*100) // 10
# one = (x - hun*100 - ten*10) // 1
# new_x = one * 100 + ten * 10 + hun * 1
#
# print(new_x)

# x = 345
# hun = x // 100
# ten = (x // 10) % 10
# one = x % 10
# new_x = one * 100 + ten * 10 + hun * 1
#
# print(hun,ten,one)

def solution(test_string):
    # YOUR CODE HERE
    log_list = test_string.split('\n')
    new_str = []
    for i in log_list:
        name = i.split()[-1]
        new_str.append(name)
    return new_str


test_str = "2023-04-27 15:30:45 - TestCase: login_successful\n\
2023-04-27 15:35:12 - TestCase: invalid_password"

test_name = solution(test_str)
print(test_name)