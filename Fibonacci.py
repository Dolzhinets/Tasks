from functools import lru_cache

#проверка правильности вводимых данных
while True:
    try:
        number = int(input('Input number: '))
        assert number > 0, 'The number must be more than 0'
        break
    except ValueError:
        print('Wrong input, please try again')
        continue
    except AssertionError as error:
        print(error)
        continue

"""функция для вычисления числа Фибоначчи с кэшированием для более 
высокой скорости при вводе больших чисел"""
@lru_cache(number)
def Fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return Fibonacci(number - 1) + Fibonacci(number - 2)

print([Fibonacci(i) for i in range(number)])

