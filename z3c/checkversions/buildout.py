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

from zc.buildout.buildout import Buildout
from z3c.checkversions import base


class Checker(base.Checker):
    """checker class for a buildout
    """
    def get_versions(self):
        buildout = Buildout(self.filename, '')

        # set the index URL from the buildout if not already provided
        buildout_index = buildout['buildout'].get('index')
        if not self.__custom_url:
            self._set_index_url(buildout_index)

        print(u"Checking buildout file %s" % self.filename)
        return buildout['versions']


