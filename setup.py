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

from setuptools import setup, find_packages

setup(
    name='z3c.checkversions',
    version='1.0',
    description="Find newer package versions on PyPI",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Buildout',
        'Framework :: Zope :: 2',
        'Framework :: Zope :: 3',
        'Framework :: Zope :: 4',
        'Framework :: Zope2',
        'Framework :: Zope3',
    ],
    keywords='version, buildout, packages, upgrade, zope, ztk',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='http://pypi.python.org/pypi/z3c.checkversions',
    license='ZPL 2.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['z3c'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools >= 8',
    ],
    extras_require={
        'buildout': ['zc.buildout'],
    },
    tests_require=['zc.buildout'],
    test_suite='z3c.checkversions.test.test_suite',
    entry_points="""
    [console_scripts]
    checkversions = z3c.checkversions.main:main
    """,
)
