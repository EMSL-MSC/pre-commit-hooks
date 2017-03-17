from __future__ import print_function

import argparse
import sys
from subprocess import call

def check_cookstyle(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='cookstyle filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        if filename[-3:] == '.rb':
            if call(['cookstyle', '-a', '-D', filename]) != 0:
                print('{0}: Failed to run cookstyle.'.format(filename))
                retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_cookstyle())
