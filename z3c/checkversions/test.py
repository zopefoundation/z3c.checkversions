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
import os
import tempfile

def write_temp_file(content):
    fd, path = tempfile.mkstemp(prefix='test-z3c.checkversions-')
    f = os.fdopen(fd, 'w')
    f.write(content)
    f.close()
    return path

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
