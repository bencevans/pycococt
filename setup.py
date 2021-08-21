#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(
    name='pycococt',
    description='Python interface to the COCO-CameraTrap datasets.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=['pycococt'],
    package_dir={'pycococt': 'pycococt'},
    install_requires=[
        'pycocotools>=2.0.0'
    ],
    version='0.1'
)
