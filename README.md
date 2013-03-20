pyfacter
========

A Puppet fact-write written in Python.

    $ ./pyfacter.py -h
    usage: pyfacter.py [-h] [--facter_path FACTER_PATH] fact value

    positional arguments:
      fact                  The fact you want to add.
      value                 The value you want to store for the fact.

    optional arguments:
      -h, --help            show this help message and exit
      --facter_path FACTER_PATH
                            The path to where you want to write the facts.
