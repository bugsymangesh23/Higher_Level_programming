#!/usr/bin/python3
'''
Write a function that prints the last digit of a number.
Prototype: def print_last_digit(number):
Returns the value of the last digit
You are not allowed to import any module
'''
def print_last_digit(number):
    if number < 0:
        last_digit = number % -(10)
        print(-(last_digit), end='')
    else:
        last_digit = number % 10
        print(last_digit, end='')
    return abs(last_digit) 
