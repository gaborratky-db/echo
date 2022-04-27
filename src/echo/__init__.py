import sys

from argparse import ArgumentError


def main():
    print('sys.argv[1:]', sys.argv[1:])
    for arg in sys.argv:
        if arg == 'throw' or arg == '--throw=poop':
            raise ArgumentError("💩")
