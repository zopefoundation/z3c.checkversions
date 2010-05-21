Introduction
============

Find newer versions of your installed Python packages, or newer versions of
packages in a buildout file.

This package provides a console script named ``checkversions``.

Install
=======

you can install this package either in a virtualenv::

    $ virtualenv sandbox
    $ sandbox/bin/pip install z3c.checkversions
    $ sandbox/bin/checkversions --help

or in your system::

    $ sudo pip install z3c.checkversions
    $ checkversions --help

or in a buildout::

    [buildout]
    parts = checkversions
    
    [checkversions]
    recipe=zc.recipe.egg
    eggs=z3c.checkversions


Usage
=====

::

    $ checkversions -h
    Usage: checkversions [options]
    
    This script will check new package versions of either your current installed
    distributions or a buildout file if provided. It can detect major or minor
    versions availability: level 0 gets the highest version (X.y.z), level 1 gets
    the highest intermediate version (x.Y.z), level 2 gets the highest minor
    version (x.y.Z).  Using level 2, you can automatically retrieve all bugfix
    versions of a buildout.
    
    Options:
      -h, --help            show this help message and exit
      -l LEVEL, --level=LEVEL
                            Version level to check
      -i INDEX, --index=INDEX
                            Alternative package index URL
      -v, --verbose         Verbose mode (prints old versions too)


Examples
========

For installed packages
----------------------

Example with a virtualenv::

    $ virtualenv --no-site-packages sandbox
    $ sandbox/bin/pip install z3c.checkversions
    $ sandbox/bin/checkversions -v -l 1
    # Checking your installed distributions
    pip=0.7.1 # was: 0.6.3

For a buildout
--------------

It can work either with a full buildout.cfg or with a simple versions.cfg file.

Here is a sample `versions.cfg` file::

    [versions]
    pip=0.6.3

You can create a new versions.cfg with the output ::

    $ checkversions -v -l 1 versions.cfg
    # Checking your installed distributions
    pip=0.7.1 # was: 0.6.3



