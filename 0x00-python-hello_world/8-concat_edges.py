#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
output = str.split()
print(' '.join(output[5:8])  +  ' with '  + output[0])
