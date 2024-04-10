import sys

from argparse import ArgumentError, ArgumentParser


def main():
    print('sys.argv[1:]', sys.argv[1:])
    for arg in sys.argv:
        if arg == 'throw' or arg == '--throw=error':
            raise RuntimeError("error")


def main_with_args(*args, **kwargs):
    print('*args', args)
    print('**kwargs', kwargs)
    for arg in args:
        if arg == 'throw' or arg == '--throw=error':
            raise RuntimeError("error")

    if kwargs.get('throw') == 'error':
        raise RuntimeError("error")


def parse_with_args():
    parser = ArgumentParser(description='Echo arguments')
    parser.add_argument('args', nargs='*')
    parser.add_argument('--throw', action='store', help='Throw an error')
    # Only parse known args, ignore unknown arguments:w
    args, leftovers = parser.parse_known_args()
    print('args', args)
    print('leftovers', leftovers)

    if args.throw is not None and args.throw == 'error':
        raise RuntimeError("error")
