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

from setuptools import setup


setup(
    name='z3c.checkversions',
    version='3.1.dev0',
    description="Find newer package versions on PyPI",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Buildout',
        'Framework :: Zope',
        'Framework :: Zope :: 3',
        'Framework :: Zope :: 5',
    ],
    keywords='version, buildout, packages, upgrade, zope, ztk',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    url='https://github.com/zopefoundation/z3c.checkversions',
    license='ZPL-2.1',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools >= 8',
    ],
    python_requires='>=3.9',
    extras_require={
        'buildout': ['zc.buildout'],
        'test': ['zope.testing'],
    },
    entry_points="""
    [console_scripts]
    checkversions = z3c.checkversions.main:main
    """,
)
