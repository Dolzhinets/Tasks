from math import * #импортируем модуль math
import numpy as np #импортируем библиотеку numpy для импорта кубического корня - np.cbrt 

a, b, c, d = int(input('Введите а ')), int(input('Введите b ')), int(input('Введите с ')), int(input('Введите d '))

# расчет кубического уравнения взят с сайта - https://ru.intemodino.com/math/algebra/equations/cardano%27s-formula-for-solving-cubic-equations.html

p = (3 * a * c - b ** 2) / (3 * a ** 2)
q = ((2 * b ** 3) - (9 * a * b * c) + (27 * (a ** 2) * d))/ (27 * a ** 3)
Q = (p / 3) ** 3 + (q / 2) ** 2 

if Q < 0: #3 действительных корня
    if q > 0:
        t = atan(sqrt(-Q) / (-q / 2)) + pi
        x1 = 2 * sqrt(- p / 3) * cos (t / 3) - (b / (3 * a))
        x2 = 2 * sqrt(- p / 3) * cos (t / 3 + (2 * pi / 3)) - (b / (3 * a))
        x3 = 2 * sqrt(- p / 3) * cos (t / 3 + (4 * pi / 3)) - (b / (3 * a))
    elif q < 0:
        t = atan(sqrt(-Q) / (-q / 2)) 
        x1 = 2 * sqrt(- p / 3) * cos (t / 3) - (b / (3 * a))
        x2 = 2 * sqrt(- p / 3) * cos (t / 3 + (2 * pi / 3)) - (b / (3 * a))
        x3 = 2 * sqrt(- p / 3) * cos (t / 3 + (4 * pi / 3)) - (b / (3 * a))
    elif q == 0:
        t = pi / 2 
        x1 = 2 * sqrt(- p / 3) * cos (t / 3) - (b / (3 * a))
        x2 = 2 * sqrt(- p / 3) * cos (t / 3 + (2 * pi / 3)) - (b / (3 * a))
        x3 = 2 * sqrt(- p / 3) * cos (t / 3 + (4 * pi / 3)) - (b / (3 * a))

elif Q == 0: #2 действительных корня
    x1 = 2 * np.cbrt(- q / 2)  - (b / (3 * a))
    x2 =  - np.cbrt(-q / 2)  - (b / (3 * a))
    x3 = ""

elif Q > 0: #1 действительный корень и два комплексно сопряженных
    x1 = np.cbrt(- q / 2 + sqrt(Q))  + np.cbrt(-q / 2 - sqrt(Q))  - (b / (3 * a))
    x2 = (- 1 / 2) * (np.cbrt(- q / 2 + sqrt(Q)) + np.cbrt(-q / 2 - sqrt(Q))) + 1j * ((sqrt(3) / 2) * (np.cbrt(- q / 2 + sqrt(Q)) - np.cbrt(-q / 2 - sqrt(Q)))) - (b / (3 * a))
    x3 = (- 1 / 2) * (np.cbrt(- q / 2 + sqrt(Q)) + np.cbrt(-q / 2 - sqrt(Q))) - 1j * ((sqrt(3) / 2) * (np.cbrt(- q / 2 + sqrt(Q)) - np.cbrt(-q / 2 - sqrt(Q)))) - (b / (3 * a))
print(x1, x2, x3)
