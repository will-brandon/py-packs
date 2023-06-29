import setuptools

VERSION = '0.1.0'
DESC = 'Web module configuration service'
LONG_DESC = 'Web module configuration service using Docker Compose'

setuptools.setup(
    name='stax',
    version='0.0.1',
    description=DESC,
    long_description=LONG_DESC,
    license='GPL v3',
    author='Will Brandon',
    packages=['stax'],
    package_data={
        'stax': ['info.txt']
    },
    url='git@github.com:will-brandon/stax.git',
    install_requires=['pywbu'],
    entry_points = {
        'console_scripts': [
            'stax=stax.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X'
        'Operating System :: Linux :: Ubuntu',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6'
    ]
)