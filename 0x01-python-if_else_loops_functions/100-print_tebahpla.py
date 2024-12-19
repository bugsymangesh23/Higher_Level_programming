#!/usr/bin/python3
'''
Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module
'''
for i in range(ord('z'), ord('a')-1,-1):
    if i % 2 == 0:
        diff = 0
    else:
        diff = 32
    print("{}".format(chr(i - diff)), end='')
