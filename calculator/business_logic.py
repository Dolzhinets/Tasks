import data 


def validation(user_input):
    for i in user_input:
        if i in '1234567890().' or i in data.operators:
            continue
        else:
            return None
    else:
        return user_input


def calculation(expression):
    number = ''
    for i in expression:
        if i in '1234567890.':
            number += i
        elif number:
            yield float(number)
            number = ''
        elif not number and i in '-':
            number += i
            continue
        if i in data.operators or i in '()':
            yield i
    if number:
        yield float(number)


def mixed(expression):
    list_1 = []
    for i in expression:
        if i in data.operators:
            while list_1 and list_1[-1] != '(' and data.operators[i][0] <= data.operators[list_1[-1]][0]:
                yield list_1.pop()
            list_1.append(i)
        elif i == ')':
            while list_1:
                x = list_1.pop()
                if x == '(':
                    break
                yield x
        elif i == '(':
            list_1.append(i)
        else:
            yield i
    while list_1:
        yield list_1.pop()


def calculator(sorted_calc):
    list_1= []
    for i in sorted_calc:
        try:
            if i in data.operators:
                z = list_1.pop()
                y = list_1.pop()
                list_1.append(data.operators[i][1](y, z))
            else:
                list_1.append(i)
        except ZeroDivisionError:
            return -1
    return list_1[0]