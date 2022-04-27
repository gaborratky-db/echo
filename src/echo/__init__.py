import sys

from argparse import ArgumentError


def main():
    print('sys.argv[1:]', sys.argv[1:])
    if sys.argv[1] == 'throw' or sys.argv[1] == '--throw=poop':
        raise ArgumentError("💩")
