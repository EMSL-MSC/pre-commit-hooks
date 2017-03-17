from __future__ import print_function

import argparse
import sys
from subprocess import call


def check_rspec(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='JSON filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    specs_to_run = []
    for filename in args.filenames:
        if filename[-3:] == '.rb' and filename[:8] == 'recipes/':
            specs_to_run.append('spec/unit/recipes/{}_spec.rb'.format(filename[8:-3]))
        if filename[-3:] == '.rb' and filename[:18] == 'spec/unit/recipes/':
            specs_to_run.append(filename)
    if len(specs_to_run) and call(['rspec'] + specs_to_run) != 0:
        print('Failed to rspec recipe.')
        retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_rspec())
