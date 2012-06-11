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
import distutils.log

def setUp(test):
    test._old_log_level = distutils.log.set_threshold(distutils.log.ERROR)

def tearDown(test):
    distutils.log.set_threshold(test._old_log_level)

def test_suite():
    optionflags = ELLIPSIS|NORMALIZE_WHITESPACE
    suite = DocFileSuite('README.txt', 'buildout.txt', 'installed.txt',
                         setUp=setUp, tearDown=tearDown,
                         optionflags=optionflags)
    return suite
