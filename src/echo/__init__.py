import sys


def main():
    print('sys.argv[1:]', sys.argv[1:])


def main_with_args(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)
    print('sys.argv[1:]', sys.argv[1:])
