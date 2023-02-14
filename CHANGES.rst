Changelog
=========

2.0 (2023-02-14)
----------------

- Add support for Python 3.10, 3.11.

- Drop support for Python 2.7, 3.5, 3.6.

- Pin ``setuptools < 66`` as newer versions are no longer compatible.


1.2 (2020-04-13)
----------------

- Add support for Python 3.8, drop support for Python 3.4.

- Improve error message in case zc.buildout is not installed.

- Improve installation instruction.

- Pass the index url to both the 'installed' and 'buildout' checkers.


1.1 (2018-11-03)
----------------

- Add support for Python 3.7.

- Drop support for `python setup.py test`.


1.0 (2018-05-23)
----------------

- Fix compatibility with setuptools 39 by using an API introduced
  in setuptools 8. (`GH #8`_)

- Add support for Python 3.5, 3.6 and PyPy3.

- Drop support for Python 2.6 and 3.3.

- Standardize namespace ``__init__``.

.. _GH #8 : https://github.com/zopefoundation/z3c.checkversions/issues/8


0.5 (2014-09-15)
----------------

- Python 3 support by Nicolas Dietrich (`GH #2`_, `GH #4`_)

.. _GH #2: https://github.com/zopefoundation/z3c.checkversions/pull/2
.. _GH #4: https://github.com/zopefoundation/z3c.checkversions/pull/4

0.4.2 (2013-10-02)
------------------

- ignore installed packages while searching for new versions, only look in
  the package index (makes the test suite more reliable, among other things).
- fix IndexError: list index out of range when buildout.cfg had a package with
  a blank version pin.
- show updates for non-final package versions, if there's a newer non-final
  version available on PyPI (`GH #1`_)

.. _GH #1: https://github.com/zopefoundation/z3c.checkversions/pull/1

0.4.1 (2010-08-25)
------------------

- fixed edge case bug where 1.0 was never updated to 1.0.x
- warn buildout users about the extra requirement

0.4 (2010-07-26)
----------------

- added a `blacklist` option for passing versions to avoid
  (possibly coming from a buildbot)
- added a `incremental` option to suggest only one upgrade
- remove a temporary file during tests

0.3 (2010-07-09)
----------------

- don't accumulate old comments
- prefer final versions

0.2 (2010-05-22)
----------------

- added a verbose option to print old versions as well
- updated metadata, doc and license

0.1 (2010-05-16)
----------------

- Initial release
