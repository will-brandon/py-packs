"""
setup.py

Type:   Python Package Setup Script
Author: Will Brandon
Date:   June 23, 2023

Builds and installs the pywbu module.
"""

import setuptools


# Use setuptools to build or install the module.
setuptools.setup(
    name='pywbu',
    version='1.0.0',
    description='Python general utilities library',
    long_description='Python general utilities library for file IO, console IO, etc.',
    url='git@github.com:will-brandon/py-packs.git',
    license='GPL v3',
    author='Will Brandon',
    packages=['src'],
    py_modules=['console'],
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X'
        'Operating System :: Unix',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6'
    ]
)
