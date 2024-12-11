#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    return 98 + (a ** b)

# Disassemble the function to view its bytecode
dis.dis(magic_calculation)

