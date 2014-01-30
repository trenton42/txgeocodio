#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='txgeogodio',
    version='0.1.0',
    description='Fetch and cache address geocoding',
    long_description=readme + '\n\n' + history,
    author='Trenton Broughton',
    author_email='trenton@kindrid.com',
    url='https://github.com/trenton42/txgeogodio',
    packages=[
        'txgeogodio',
    ],
    package_dir={'txgeogodio': 'txgeogodio'},
    include_package_data=True,
    install_requires=[
        'treq',
        'wrapt'
    ],
    license="BSD",
    zip_safe=False,
    keywords='txgeogodio',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='trial',
)