from doctest import DocFileSuite, ELLIPSIS, NORMALIZE_WHITESPACE
import unittest

def test():
    optionflags = ELLIPSIS|NORMALIZE_WHITESPACE
    suite = unittest.TestSuite()
    suite.addTest(DocFileSuite('README.txt', optionflags=optionflags))
    suite.addTest(DocFileSuite('buildout.txt', optionflags=optionflags))
    suite.addTest(DocFileSuite('installed.txt', optionflags=optionflags))

    return suite
