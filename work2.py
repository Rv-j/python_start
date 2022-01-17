#1. Construct an integer from the string "123"
a = '123'
c = int(a)
print(c)

#2. Construct a float from the integer 123
a = 123
c = float(a)
print(c)


#3. Construct an integer from the float 12.345
a = 12.345
c = int(a)
print(c)

#4. Write a Python-script that detects the last 4 digits of a credit card
x = int(input('x='))
a = x // 1000 % 10
b = x // 100 % 10
c = x // 10 % 10
d = x % 10
print(a,b,c,d)
#5. Write a Python-script that calculates the sum of the digits of a three-digit
#number
y = int(input('y='))
y = x // 100
y = x // 10 % 10
y = x % 10
print(a + b + c)

#6. Write a program that calculates and displays the area of a triangle if its sides
#are known
import math
a = 3
b = 4
c = 5
p = (a + b + c)/2
s = p*(p-a)*(p-b)*(p-c)
s = math.sqrt(s)
print(s)
#7. *Write a Python-script that calculates the sum of the digits of a number

#8. *Determine the number of digits in a number

#9. *Print the digits in reverse order