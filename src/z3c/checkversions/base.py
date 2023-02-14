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

from pkg_resources import Requirement
from pkg_resources import parse_version

from setuptools import package_index


def _final_version(parsed_version):
    """Function copied from zc.buildout.easy_install._final_version."""
    return not parsed_version.is_prerelease


class Checker:
    """Base class for version checkers

    attributes:

    index_url: url of an alternative package index
    verbose: display every version, not only new ones,
             and display the previous version as a comment
    blacklist: filename of the blacklist
    incremental: suggest only one package upgrade
    """

    __custom_url = False

    def __init__(self,
                 index_url=None,
                 verbose=False,
                 blacklist=None,
                 incremental=False):
        self.verbose = verbose
        self.incremental = incremental
        if blacklist:
            # create a set of tuples with bad versions
            with open(blacklist) as b:
                self.blacklist = {
                    tuple(map(lambda x: x.strip(), line.split('=')))
                    for line in b.readlines()
                    if '=' in line
                }
        else:
            self.blacklist = set()
        self.pi = package_index.PackageIndex(search_path=())
        self._set_index_url(index_url)
        if index_url is not None:
            self.__custom_url = True

    def _set_index_url(self, url):
        """Set the index URL."""
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

        for name, version in sorted(versions.items()):
            if self.incremental == 'stop':
                # skip subsequent scans
                print("{}={}".format(name, version))
                continue
            parsed_version = parse_version(version)
            req = Requirement.parse(name)
            self.pi.find_packages(req)
            new_dist = None
            # loop all index versions until we find the 1st newer version
            # that keeps the major versions (below level)
            # and is a final version
            # and is not in the blacklist
            for dist in self.pi[req.key]:
                if self.incremental == 'stop':
                    continue
                if (dist.project_name, dist.version) in self.blacklist:
                    continue
                if (_final_version(parsed_version)
                        and not _final_version(dist.parsed_version)):
                    # only skip non-final releases if the current release is
                    # a final one
                    continue
                # trunk the version tuple to the first `level` elements
                trunked_current = (
                    parsed_version.base_version.split('.')[:level])
                trunked_candidate = (
                    dist.parsed_version.base_version.split('.')[:level])
                while len(trunked_candidate) < level:
                    trunked_candidate.append('00000000')
                while len(trunked_current) < level:
                    trunked_current.append('00000000')
                # ok now we can compare: -> skip if we're still higher.
                if trunked_candidate > trunked_current:
                    continue
                new_dist = dist
                break

            if new_dist and new_dist.parsed_version > parsed_version:
                if self.incremental is True:
                    self.incremental = 'stop'
                if self.verbose:
                    print("{}={} # was: {}".format(
                        name, new_dist.version, version))
                else:
                    print("{}={}".format(name, new_dist.version))
            elif self.verbose:
                print("{}={}".format(name, version))

    def get_versions(self):
        """Get a dict {'name': 'version', ...} with package versions to check.

        This should be implemented by derived classes
        """
        raise NotImplementedError
