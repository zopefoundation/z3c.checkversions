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

from pkg_resources import parse_version, Requirement
from setuptools import package_index


_final_parts = '*final-', '*final'
def _final_version(parsed_version):
    """Function copied from zc.buildout.easy_install._final_version

    >>> 1+1
    >>>
    """
    for part in parsed_version:
        if (part[:1] == '*') and (part not in _final_parts):
            return False
    return True


class Checker(object):
    """Base class for version checkers
    """
    __custom_url = False
    def __init__(self, index_url=None, verbose=False):
        self.verbose = verbose
        self.pi = package_index.PackageIndex()
        self._set_index_url(index_url)
        if index_url is not None:
            self.__custom_url = True

    def _set_index_url(self, url):
        """set the index URL
        """
        if url is not None:
            self.pi.index_url = url
        if not self.pi.index_url.endswith('/'):
            self.pi.index_url += '/'

    def check(self, level=0):
        """Search new versions in a version list
        versions must be a dict {'name': 'version'}

        The new version is limited to the given level:
        Example with version x.y.z
        level = 0: checks new version x
        level = 1: checks new version y
        level = 2: checks new version z

        By default, the highest version is found.
        """
        versions = self.get_versions()

        for name, version in versions.items():
            parsed_version = parse_version(version)
            req = Requirement.parse(name)
            self.pi.find_packages(req)
            new_dist = None
            # loop all index versions until we find the 1st newer version
            # that keeps the major versions (below level)
            # and is a final version
            for dist in self.pi[req.key]:
                if not _final_version(dist.parsed_version):
                    continue
                if dist.parsed_version[:level] > parsed_version[:level]:
                    continue
                new_dist = dist
                break

            if new_dist and new_dist.parsed_version > parsed_version:
                if self.verbose:
                    print("%s=%s # was: %s"
                          % (name, new_dist.version, version.split()[0]))
                else:
                    print("%s=%s" % (name, new_dist.version))
            elif self.verbose:
                print("%s=%s" % (name, version.split()[0]))


    def get_versions(self):
        """Get a dict {'name': 'version', ...} with package versions to check.
        This should be implemented by derived classes
        """
        raise NotImplementedError
