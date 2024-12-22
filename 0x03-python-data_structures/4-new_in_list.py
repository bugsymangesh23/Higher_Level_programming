#!/usr/bin/python3
'''
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
Prototype: def new_in_list(my_list, idx, element):
If idx is negative, the function should return a copy of the original list
If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except
'''
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for elm in my_list[::-1]:
            print("{:d}".format(elm))
