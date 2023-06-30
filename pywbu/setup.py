"""
setup.py

Type:       Python Package Setup Script
Author:     Will Brandon
Created:    June 23, 2023
Revised:    June 30, 2023

Builds and installs the pywbu package.
"""

import setuptools


# Use setuptools to build or install the package.
setuptools.setup(
    name='pywbu',
    version='1.0.0',
    description='Python general utilities library',
    long_description='Python general utilities library for file IO, console IO, etc.',
    url='git@github.com:will-brandon/py-packs.git',
    license='GPL v3',
    author='Will Brandon',
    packages=['pywbu'],
    py_modules=['console'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X'
        'Operating System :: Unix',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6'
    ]
)
