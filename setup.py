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
    name='txgeocodio',
    version='0.1.0',
    description='Fetch and cache address geocoding',
    long_description=readme + '\n\n' + history,
    author='Trenton Broughton',
    author_email='trenton@kindrid.com',
    url='https://github.com/trenton42/txgeocodio',
    packages=[
        'txgeocodio',
    ],
    package_dir={'txgeocodio': 'txgeocodio'},
    include_package_data=True,
    install_requires=[
        'treq',
        'wrapt'
    ],
    license="BSD",
    zip_safe=False,
    keywords='txgeocodio',
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
