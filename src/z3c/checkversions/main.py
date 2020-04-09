##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""This script will check new package versions of either
your current installed distributions or a buildout file if provided.
It can detect major or minor versions availability:
level 0 gets the highest version (X.y.z),
level 1 gets the highest intermediate version (x.Y.z),
level 2 gets the highest minor version (x.y.Z).

Using level 2, you can automatically retrieve all bugfix versions of a
buildout.

If you provide a blacklist file with bad versions, these versions won't be
suggested.
"""

from __future__ import absolute_import

from optparse import OptionParser
import os


def main():
    usage = (
        u"Usage: %prog [-v] [-l LEVEL] [-i INDEX] [-b BLACKLIST] [-1]"
        u" [buildout_file]")
    parser = OptionParser(description=__doc__, usage=usage)

    parser.add_option('-l', '--level',
                      type='int',
                      dest='level',
                      default=0,
                      help=u"Version level to check")

    parser.add_option('-i', '--index',
                      dest='index',
                      help=u"Provide and alternative package index URL")

    parser.add_option('-b', '--blacklist',
                      dest='blacklist',
                      default="",
                      help=u"Provide a blacklist file with bad versions")

    parser.add_option('-1', '--incremental',
                      dest='incremental',
                      action='store_true',
                      default=False,
                      help=u"Suggest only one upgrade. Skip others.")

    parser.add_option('-v', '--verbose',
                      dest='verbose',
                      action='store_true',
                      default=False,
                      help=u"Verbose mode (prints old versions too)")
    options, args = parser.parse_args()

    if len(args) > 1:
        parser.error("You must specify only one argument")

    if options.blacklist != "" and not os.path.exists(options.blacklist):
        parser.error(
          'The blacklist file "%s" does not exist!' % options.blacklist)

    kw = {}
    if options.index is not None:
        kw['index_url'] = options.index

    if len(args) == 1:
        from . import buildout
        kw['filename'] = args[0]
        factory = buildout.Checker
    else:
        from . import installed
        factory = installed.Checker

    checker = factory(blacklist=options.blacklist,
                      incremental=options.incremental,
                      verbose=options.verbose,
                      **kw)
    checker.check(level=options.level)


if __name__ == '__main__':
    main()
