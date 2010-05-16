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


