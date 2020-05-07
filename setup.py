#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pycococt',
    packages=['pycococt'],
    package_dir = {'pycococt': 'pycococt'},
    install_requires=[
        'pycococt>=2.0.0'
    ],
    version='0.0'
)