from __future__ import print_function

import argparse
import sys
from subprocess import call


def check_rspec(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='JSON filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        spec_to_run = None
        if filename[-3:] == '.rb' and filename[:8] == 'recipes/':
            spec_to_run = 'spec/unit/recipes/{}_spec.rb'.format(filename[8:-3])
        if filename[-3:] == '.rb' and filename[:18] == 'spec/unit/recipes/':
            spec_to_run = filename
        if spec_to_run and call(['rspec', spec_to_run]) != 0:
            print('{0}: Failed to rspec recipe.'.format(filename))
            retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_rspec())
