"""
setup.py

Type:   Python Package Setup Script
Author: Will Brandon
Date:   June 23, 2023

Builds and installs the pyutils pip module.
"""

import setuptools


# Use setuptools to build / install the module.
setuptools.setup(
    name='pywbu',
    version='1.0.0',
    description='Python general utilities library',
    long_description='Python general utilities library for file IO, console IO, etc.',
    license='GPL v3',
    author='Will Brandon',
    packages=['pywbu'],
    py_modules=['console'],
    url='git@github.com:will-brandon/pywbu.git',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X'
        'Operating System :: Unix',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6'
    ]
)
