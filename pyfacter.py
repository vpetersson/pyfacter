#!/usr/bin/env python
# -*- coding: utf8 -*-

import argparse
import os

# The path appears to work for Debian-derived systems.
default_facter_path = '/usr/local/lib/site_ruby/facter'


def fact_writer(fact, value, facter_path=default_facter_path):

    if not os.path.isdir(facter_path):
        os.mkdir(facter_path)

    fact_file = os.path.join(facter_path, fact + '.rb')
    fact_file_content = "# %s.rb\nFacter.add('%s') do\n  setcode do\n    '%s'\n  end\nend" % (fact, fact, value)

    f = open(fact_file, 'w')
    f.write(fact_file_content)
    f.close()

if __name__ == "__main__":
    # Argument parser block
    parser = argparse.ArgumentParser()
    parser.add_argument("fact", help="The fact you want to add.")
    parser.add_argument("value", help="The value you want to store for the fact.")
    parser.add_argument("--facter_path", help="The path to where you want to write the facts. Defaults to '%s'." % default_facter_path, default=default_facter_path)
    args = parser.parse_args()

    # Do your thing...
    fact_writer(args.fact, args.value, args.facter_path)
