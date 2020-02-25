#!/usr/bin/env python3.8

def add(num1, num2):
    result = int(num1+num2)
    return result
    
def minus(num1, num2):
    result = int(num1 - num2)
    return result

def multiply(num1, num2):
    result = int(num1 * num2)
    return result

def divide(num1, num2):
    result = float(num1/num2)
    return result

def  inputs():
    operation = input("Choose an operation \n + (plus) \n - (minus) \n * (multiply) \n / (divide) \n")
    num1 = int (input("enter your first number:"))
    num2 = int (input("enter your second number:"))
    return operation, num1, num2

def calculation(operation, num1, num2):
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = minus(num1, num2)
    elif operation == '*':
        result = multiply (num1, num2)
    elif operation =='/':
        result = divide(num1, num2)
    return result

def answer(result):
    print("answer = " + str(result))

operation, num1, num2  = inputs()
result = calculation(operation, num1, num2)
answer(result)

