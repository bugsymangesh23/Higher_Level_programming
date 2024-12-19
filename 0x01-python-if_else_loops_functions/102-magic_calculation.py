#!/usr/bin/python3
'''
Write the Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
'''
def magic_calculation(a, b, c):
    if a < b:
        return(c)
    if c > b:
        return(a+b)
    return (a*b-c)

