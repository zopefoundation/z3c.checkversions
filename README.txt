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

For installed packages
----------------------

Imagine `foobar` 1.0.1 is installed in your system

Check the highest versions available::

    $ checkversions
    foobar=2.3.5

Check the highest intermediate upgrades available::

    $ checkversions -l 1
    foobar=1.4.2

Check the highest minor upgrades available::

    $ checkversions -l 2
    foobar=1.0.5

For a buildout
--------------

The usage is the same, you just have to specify the buildout file to scan.
The buildout does not need to be built.

Imagine you have a buildout.cfg with::

    [versions]
    foobar=1.0.0

Check the highest versions available::

    $ checkversions buildout.cfg
    foobar=2.3.5

Check the highest intermediate upgrades available

    $ checkversions -l 1 buildout.cfg
    foobar=1.4.2

Check the highest minor upgrades available

    $ checkversions -l 2 buildout.cfg
    foobar=1.0.5


