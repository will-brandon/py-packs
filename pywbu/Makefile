# Makefile
#
# Type:		GNU Makefile
# Author:	Will Brandon
# Date: 	June 28, 2023
#
# Builds, installs, uninstalls, and cleans the pywbu package.
#
# Usage:	make

# Define the package name.
PACKAGE=pywbu

# This is the default target. This target builds and installs the package to pip.
start: build install

# This target builds the package..
build:
	python3 setup.py build

# This target installs the package to pip.
install:
	python3 setup.py install

# This target removes the package from pip and cleans out the build.
purge: uninstall clean

# This target removes the package from pip.
uninstall:
	pip3 uninstall -y ${PACKAGE}

# This target cleans out the package build.
clean:
	rm -rf build
	rm -rf dist
	rm -rf ${PACKAGE}.egg-info
	rm -rf ${PACKAGE}/__pycache__

# All targets are phony i.e. do not refer to literal files.
.PHONY: start build install purge uninstall clean
