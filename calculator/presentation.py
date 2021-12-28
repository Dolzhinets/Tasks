from business_logic import validation, calculation, mixed, calculator


def show_message(message):
    print(message)


def get_result(expression):
    result = calculator(mixed(calculation(expression)))
    if result == -1:
        return show_message('ZeroDivisionError')
    return show_message(f'Answer: {result}')


if __name__ == '__main__':
    show_message('Enter expression:')
    while True:
        valid_input = validation(input())
        if valid_input:
            get_result(valid_input)
            break
        else:
            show_message('Input error\nTry again:')
            continue