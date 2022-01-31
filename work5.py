'''1)Выведите на экран все числа в диапазоне от 1 до 100 кратные 7.'''
for n in range(1, 101):
    if n % 7 == 0:
        print(n)


'''2)Вычислить с помощью цикла факториал числа n введенного с
клавиатуры (4<n<16). Факториал числа - это произведение всех чисел от
этого числа до 1. Например, 5!=5*4*3*2*1=120'''
import math

n = int(input('n='))
if 4 < n < 16:
    f = math.factorial(n)
    print(f)


'''3)Напечатайте таблицу умножения на 5. Предпочтительно печатать 1 x 5
= 5, 2 x 5 = 10, а не просто 5, 10 и т. д.'''
a = 0
while a < 10:
    a += 1
    print('5 *', a, '=', 5*a)


'''4)Выведите на экран прямоугольник из *. Причем, высота и ширина
#прямоугольника вводятся с клавиатуры. Например, ниже представлен
#прямоугольник с высотой 4 и шириной 5.
*****
*   *
*   *
*****'''
a = int(input('height: '))
b = int(input('while: '))
c = 1
while c <= a:
    d = 1
    while d <= b:
        if c == 1 or d == 1 or c == a or d == b:
            print('*', end=' ')
        else:
            print(' ', end=' ')
        d = d + 1
    c = c + 1
    print()

'''5)Дан список [0,5,2,4,7,1,3,19]. Написать программу для подсчета нечетных цифр в нем.'''
list = [0,5,2,4,7,1,3,19]
n = 0
for a in list:
    if a % 2 != 0:
        n = n + 1
print(n)

'''6)Создайте список случайных чисел (размером 4 элемента). Создайте второй список в
два раза больше первого, где первые 4 элемента должны быть равны элементам
первого списка, а остальные элементы заполните удвоенными значением начальных.
Например,
Было → [1,4,7,2]
Стало → [1,4,7,2,2,8,14,4]'''
import random
matrix = []
for i in range(4):
    matrix.append(random.randint(1,10))
print(matrix)
matrix1 = matrix * 2
for element in range(0,len(matrix1),1):
    matrix1[element] = matrix1[element] * 2
matrix1[0:4] = matrix
print(matrix1)


'''7)Создайте список из 12 элементов. Каждый элемент этого списка представляет собой
зарплату рабочего за месяц (случайное число от 7500 до 15000 грн.). Выведите этот
список на экран и вычислите среднемесячную зарплату этого рабочего.'''

import random

matrix = []
for i in range(12):
    matrix.append(random.randint(7500,15000))
print(matrix)

summa = 0
for i in matrix:
    summa = summa + i
summa = summa / 12
print(summa)

'''8)Представьте в виде списка списков матрицу
[ 1, 2 , 3, 4]
[ 5, 6 , 7, 8]
[ 9,10, 11, 12]
[13,14, 15, 16]
Напишите программу, которая выведет эту матрицу на экран, вычислит и выведет
сумму элементов этой матрицы.'''

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for element in matrix:
    print(element)
summa = 0
for i in range(4):
    for j in range(4):
        summa = summa + matrix[i][j]
print(summa)

'''Дополнительное домашнее задание.
1)С помощью циклов вывести на экран все простые числа от 1 до 100. Простое число —
число, которое делится нацело только на единицу или само на себя. Первые простые
числа это — 2,3,5,7…'''
for num in range(2,101):
    if all(num % i != 0 for i in range(2,num)):
       print(num)


'''2)Выведите на экран «песочные часы», максимальная ширина которых считывается с
клавиатуры (число нечетное). В примере ширина равна 5.
*****
***
*
***
*****'''

n = int(input("Ведите цыфру : "))
for i in range(n-1, 1, -1):
    print((n-i-1)*' ', end = '')
    for j in range(1, 2*i):
        print("*", end = '')
    print()
for i in range(1,n):
    for j in range((n-1),i,-1):
        print(" ", end = '')
    for k in range(1, 2*i):
        print("*", end = '')
    print()


'''3)Написать код для зеркального переворота списка [7,2,9,4] -> [4,9,2,7].
Список может быть произвольной длины. (При выполнении задания
использовать дополнительный список нельзя).'''

import random
matrix = []
for _ in range(4):
    matrix.append(random.randint(1,10))
print(matrix)
matrix.reverse()
print(matrix)