#!/usr/bin/python3
'''
Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

Do not use the function print (with string format to display integers) more than 4 times
You have to define:
the value 10 to a variable a
the value 5 to a variable b
and use those two variables only, as arguments when calling functions (including print)
a and b must be defined in 2 different lines: a = 10 and another b = 5
Your program should call each of the imported functions. See example below for format
the word calculator_1 should be used only once in your file
You are not allowed to use * for importing or __import__
Your code should not be executed when imported
'''
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
