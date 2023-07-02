"""
setup.py

Type:       Python Package Setup Script
Author:     Will Brandon
Created:    June 23, 2023
Revised:    June 30, 2023

Builds and installs the stax package.
"""

import setuptools as setup


# Use setuptools to build or install the package.
setup.setup(
    name='stax',
    version='0.0.1',
    description='Web module configuration service',
    long_description='Web module configuration service using Docker Compose',
    url='git@github.com:will-brandon/py-packs.git',
    license='GPL v3',
    author='Will Brandon',
    packages=setup.find_packages(),
    #install_requires=['pywbu'],
    entry_points={
        'console_scripts': [
            'stax=stax.cli.cli:main'
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X'
        'Operating System :: Unix',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6'
    ]
)
