user_string = ""
check_letter = 'h'

while check_letter.lower() not in user_string.lower():

    user_string = input("Enter a string/word, that include letter 'h' or 'H': ")

    if check_letter in user_string:
        print(f"Correct! There is '{check_letter}' or '{check_letter.swapcase()}' in s a string")
    else:
        print(f"Your string does not include '{check_letter}' or '{check_letter.swapcase()}'")

