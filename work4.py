#'''Дано четырехзначное число. Проверить, является ли оно «счастливым билетом».
#Примечание: счастливым билетом называется число, в котором, при четном
#количестве цифр в числе, сумма цифр его левой половины равна сумме цифр его
#правой половины. Например, рассмотрим число 1322. Его левая половина равна
#13, а правая 22, и оно является счастливым билетом (т. к. 1 + 3 = 2 + 2).'''
x = input('n=')
print(int(x[0]) + int(x[1]) == int(x[2]) + int(x[3]))

#'''С клавиатуры вводится шестизначное число. Проверить, является ли оно
#палиндромом. Примечание: палиндромом называется число, слово или текст,
#которые одинакового читаются слева направо и справа налево. Например, это
#числа 143341, 5555, 7117 и т. д.'''

x = input('n=')
print(int(x[0]) == int(x[5]) and int(x[1]) == int(x[4]) and int(x[2]) == int(x[3]))

#'''Есть круг с центром в начале координат и радиусом 4. Пользователь вводит с
#клавиатуры координаты точки x и y. Написать программу, которая определит,
#лежит ли эта точка внутри круга или нет.'''
from math import sqrt
x = float(input('x='))
y = float(input('y='))
r = 4
r_xy = sqrt(x ** 2 + y ** 2)
print(r_xy <= r)