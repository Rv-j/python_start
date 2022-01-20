
#Homework 3
#1. Write a Python program to print the number entered by user only if the
#number entered is negative.
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#2. Write a Python program to check if the value a is less than 20 or not.
num = float(input("Enter a number: "))
if num < 20:
    print("Less")
else:
    print("More")

#3. Write a Python program to check if a given number is Zero or Not.
num = float(input("Enter a number: "))
if num == 0:
    print("Yes")
else:
    print("Not")

#4. Write a Python program to check if a given number is Even or Odd.
num = int(input('Enter any number to test whether it is odd or even:'))
if (num % 2) == 0:
    print('The number is even')
else:
    print('The provided number is odd')


#5. Write a Python program to find largest number among three numbers
#entered by user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3
print("The largest number is",largest)