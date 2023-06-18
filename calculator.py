"""
Write a program that performs simple arithmetic operations on two numbers.
"""
"""
Create a new file called calculator.py. 
In the file, define four functions: add, subtract, multiply, and divide. 
Each function should take two arguments (the numbers to perform the operation on) 
and return the result of the operation. 
In the main part of the program, prompt the user to enter two numbers and an operation (+, -, *, /). 
Call the appropriate function based on the user's input and print the result to the console.
"""


def add():
    print(num1+num2)
    return


def subtract():
    print(num1-num2)
    return


def multiply():
    print(num1*num2)
    return


def divide():
    print(num1/num2)
    return


num1 = float(input('Enter first number: '))
operation = input('Enter operation (+, -, *, /): ')
num2 = float(input('Enter second number: '))


if operation == '+':
    add()
elif operation == '-':
    subtract()
elif operation == '*':
    multiply()
elif operation == '/':
    divide()
else:
    print("Invalid operation")
