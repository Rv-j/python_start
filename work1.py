# Exercise 1. Write a Python-script that displays the message “Hello world”.
print('Hello world')
#Exercise 2. Rewrite the first script to display three any messages.
print('One\n' 'Two\n' 'Tree\n')
#Exercise 3. Write a Python-script to reads values for the length and width of a
#rectangle and returns the area of the rectangle
length = int(input('length='))
width = int(input('width='))
print('rectangle', length * width)
#Exercise 4. Write a program that requests the user to enter two numbers and
#prints the sum, product, difference and quotient of the two numbers.
x = int(input('x='))
y = int(input('y='))
print(x + y)
print(x - y)
print(x * y)
print(x / y)
#Exercise 5. Write a program that reads in the radius of a circle and prints the
#circle’s diameter, circumference and area. Use the constant value 3.14159 for π.
#Do these calculations in output statements.
import math
r = int(input('r='))
print(math.pi * r ** 2)

