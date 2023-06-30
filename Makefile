# Makefile
#
# Type:		GNU Makefile
# Author:	Will Brandon
# Created: 	June 29, 2023
# Revised:	-
#
# Builds, installs, uninstalls, and cleans all python py-packs packages.
#
# Usage:	make

# Use Bash shell script.
SHELL := /bin/bash

# Define the package name.
PACKAGE = stax

# This is the default target. This target builds and installs all py-packs packages to pip in order
# of dependencies.
start: start-pywbu start-stax

# This target removes all py-packs packages from pip and cleans out the build.
purge: purge-stax purge-pywbu

# The following targets start and purge each package by calling submakes.
start-pywbu:
	make -C pywbu start
purge-pywbu:
	make -C pywbu purge
start-stax:
	make -C stax start
purge-stax:
	make -C stax purge

# All targets are phony i.e. do not refer to literal files.
.PHONY: start purge
