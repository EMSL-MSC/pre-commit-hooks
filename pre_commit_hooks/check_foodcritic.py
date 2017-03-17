from __future__ import print_function

import argparse
import sys
from subprocess import call


def check_foodcritic(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='JSON filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    if len(args.filenames):
        if call(['foodcritic', '--epic-fail', 'any', '.']) != 0:
            print('Failed to foodcritic the cookbook.')
            retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_foodcritic())
