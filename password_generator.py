import random
import string


def input_():
    while True:
        try:
            password_length = int(input("Input password length:\n"))
            if password_length > 0:
                break
            else:
                print('Wrong input, please try again')
        except ValueError:
            print('Wrong input, please try again')
            continue
    while True:
        special_symbols = input("Include special characters in the password? (enter y or n):\n")
        if special_symbols == "y" or special_symbols == "n":
            break
        else:
            print('Wrong input, please try again')
            continue
    return password_length, special_symbols


def random_password(password_length, special_symbols):
    spec_char = string.punctuation
    char = string.ascii_letters + string.digits
    res_password = ''
    for i in range(password_length):
        if special_symbols == "y":
            res_password += random.choice(char + spec_char)
        if special_symbols == "n":
            res_password += random.choice(char)
    return res_password


def output(password_length, special_symbols):
    while True:
        yield random_password(password_length, special_symbols)
        
if __name__ == '__main__':
    password_length, special_symbols = input_()
    password = iter(output(password_length, special_symbols))
    print('Your password:\n', next(password))