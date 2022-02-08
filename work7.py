'''1)Напишите программу, которая посчитает сколько букв «b» в введенной
строке текста.'''

my_string = 'adsbbfdfaadbfdsadbbb'
print(my.string.count('b'))



'''2)Считайте строку, которая будет представлять имя человека, введенное с
клавиатуры. Проверьте эту строку на валидность. Имеется в виду, что
например, в имени человека не может быть цифр, оно должно
начинаться с большой буквы, за которой должны следовать маленькие.'''

name = input("input name: ")
if name.isalpha() and name[0].isupper() and name[1:len(name)].islower():
    print("Valid")
else:
    print("No Valid")



'''3) Напишите программу, которая вычислит сумму всех кодов символов
строки.'''

a = input()
sum1 = 0
for i in a:
    print(ord(i))
    sum1 += ord(i)
print('sum = ', sum1)



'''4) Выведите на экран 10 строк со значением числа Pi. В первой строке
должно быть 2 знака после запятой, во второй 3 и так далее.'''

from math import pi
a = 0
while a <= 11:
    text = "pi = {{:.{}f}}".format(a)
    print(text.format(pi))
    a = a + 1



'''5) Вводится строка из слов, разделенных пробелами. Найти самое длинное
слово и вывести его на экран.'''

st = input('enter string: ').split()
count = 0
for i in st:
    if len(i) > count:
        count = len(i)
        word = i
print('the longest word is: ',word)


'''Дополнительное домашнее задание.
1)Вовочка сидя на уроке писал подряд одинаковые слова (слово может
состоять из одной буквы). Когда Марья Ивановна забрала у него тетрадь,
там была одна строка текста. Напишите программу, которая определит
самое короткое слово из написанных Вовочкой. Например:
aaaaaaa — Вовочка писал слово - «a»
ititititit — Вовочка писал слово - «it»
catcatcatcat — Вовочка писал слово - «cat»'''


s = input('text=')
s_new = ''
for i in range(len(s)):
    if s_new.find(s[i]) == -1 and s[i] != ' ':
        s_new += s[i]
print(s_new)


'''2)Напишите программу для очистки текста от html-тэгов. Больше о html-
тэгах https://html5book.ru/html-tags/
Также необходимо учесть пару особенностей:
- помимо одинарных тэгов, есть парные тэги, например <div> </div>, т.е.
первый тэг открывающий , а второй закрывающий.
- тэг внутри себя, может содержать кучу доп. информации.
Например <div id="rcnt" style="clear:both;position:relative;zoom:1">'''

import re
print re.sub(r'\<[^>]*\>', '', html)

# from bs4 import BeautifulSoup
# cleaned_string = BeautifulSoup(html_string, "lxml").text
