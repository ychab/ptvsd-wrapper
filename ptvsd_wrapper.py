#!/usr/bin/env python
import argparse
import os
import sys

import ptvsd

parser = argparse.ArgumentParser(prog='PTVSD wrapper')
parser.add_argument('--ptvsd-wait', action='store_true', dest='wait')
parser.add_argument('--ptvsd-secret', default='my_secret', dest='secret')
parser.add_argument('--ptvsd-host', default='0.0.0.0', dest='host')
parser.add_argument('--ptvsd-port', type=int, default=3000, dest='port')
args, unknown = parser.parse_known_args()


def attach():
    ptvsd.enable_attach(args.secret, address=(args.host, args.port))
    if args.wait:
        ptvsd.wait_for_attach()


def cleanup_args():
    """
    Some programs won't be happy if they got unexpected args so we need to remove
    them.
    """
    sys.argv.pop(0)  # Drop current file

    # @FIXME - Unfortunetly, didn't find a better way (like an argparse API)...
    for i, arg in enumerate(list(sys.argv)):
        if arg.startswith('--ptvsd-'):
            sys.argv.pop(i)
            if '=' not in arg and arg != '--ptvsd-wait':
                sys.argv.pop(i + 1)


def handle_django():
    if sys.argv[1] == 'runserver':
        # Disable pynotify
        if '--noreload' not in sys.argv:
            sys.argv.append('--noreload')
        # Fix cursor highlighting...
        if '--nothreading' not in sys.argv:
            sys.argv.append('--nothreading')


def main():
    attach()
    cleanup_args()

    if not sys.argv:
        parser.print_help()
        return

    script = sys.argv[0]
    # Include script path to Python path if not already.
    script_path = os.path.dirname(os.path.realpath(script))
    sys.path.append(script_path)

    # Special handling.
    if script == 'manage.py':
        handle_django()

    exec(open(script).read())


if __name__ == '__main__':
    main()
