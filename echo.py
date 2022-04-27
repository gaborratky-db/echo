import sys

from argparse import ArgumentError


print('sys.argv[1:]', sys.argv[1:])

if sys.argv[1] == 'throw':
    raise ArgumentError("💩")
