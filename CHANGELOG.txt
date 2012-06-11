Changelog
=========

0.5 (unreleased)
----------------

- print old version comment on a separate line to make generated output usable
  in buildout.
- ignore installed packages while searching for new versions, only look in
  the package index (makes the test suite more reliable, among other things).
- fix IndexError: list index out of range when buildout.cfg had a package with
  a blank version pin.

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
