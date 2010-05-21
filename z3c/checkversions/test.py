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

from doctest import DocFileSuite, ELLIPSIS, NORMALIZE_WHITESPACE
import unittest

def test():
    optionflags = ELLIPSIS|NORMALIZE_WHITESPACE
    suite = unittest.TestSuite()
    suite.addTest(DocFileSuite('README.txt', optionflags=optionflags))
    suite.addTest(DocFileSuite('buildout.txt', optionflags=optionflags))
    suite.addTest(DocFileSuite('installed.txt', optionflags=optionflags))

    return suite
