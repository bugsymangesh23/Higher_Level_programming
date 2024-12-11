#!/usr/bin/python3
import os
import py_compile
import sys

pyfile = os.getenv('PYFILE')

if not pyfile:
	print("Error: The environment variable PYFILE is not set.", file=sys.stderr)
	sys.exit(1)

try:
	print(f"Compiling {pyfile} ...")
	py_compile.compile(pyfile, cfile=pyfile + '')
except Exception as e:
	print(f"Error: {e}", file=sys.stderr)
	sys.exit(1)
