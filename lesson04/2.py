def solution(test_string):
    # YOUR CODE HERE
    log_list = test_string.split('\n')
    new_str = []
    for i in log_list:
        if "TestCase: " in i:
            name = i.split()[-1]
            print(f' Line \"{i}\" title is: {name}')
        else:
            name = i  # i.split(' ',3)[-1]
            print(f' And HERE the line \"{i}\" title is not changed: {name}')

    #return name

# test_str = "2023-04-27 15:30:45 - test PASS"
test_str = ("2023-04-27 15:30:45 - TestCase: login_successful\n\
2023-04-27 15:35:12 - TestCase: invalid_password\n\
2023-04-27 15:30:45 - test PASS")

solution(test_str)
