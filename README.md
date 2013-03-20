# pyfacter

A simple way to write Puppet facts from the command-line or in Python.

## Command-line usage

    $ ./pyfacter.py -h
    usage: pyfacter.py [-h] [--facter_path FACTER_PATH] fact value

    positional arguments:
      fact                  The fact you want to add.
      value                 The value you want to store for the fact.

    optional arguments:
      -h, --help            show this help message and exit
      --facter_path FACTER_PATH
                            The path to where you want to write the facts.

Let's try an example. Let's create a fact 'hello' with the value 'world'.

    $ sudo python pyfacter.py hello world

To verify that it worked, we can run facter:

    $ facter hello
    world

Simple as pie.

## Usage in Python

Creating facts within Python is equally easy. Just make sure you have write-access to the facter-path.

    import pyfacter
    pyfacter.fact_writer('hello', 'world')

