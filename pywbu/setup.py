"""
setup.py

Type:       Python Package Setup Script
Author:     Will Brandon
Created:    June 23, 2023
Revised:    July 2, 2023

Builds and installs the pywbu package.
"""

import setuptools as setup


# Use setuptools to build and/or install the package.
setup.setup(
    name='pywbu',
    version='1.0.0',
    description='Python general utilities library',
    long_description='Python general utilities library for file IO, console IO, etc.',
    url='git@github.com:will-brandon/py-packs.git',
    license='GPL v3',
    author='Will Brandon',
    packages=setup.find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X'
        'Operating System :: Unix',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6'
    ]
)
