"""
cli.py

Type:       Python Script
Author:     Will Brandon
Created:    June 28, 2023
Revised:    June 30, 2023

The command-line entrypoint for the stax package.
"""

from pywbu.runtime import *

@main
def main(argv: list[str]) -> int:
    
    while True:
        csl.log(argv)

    return EXIT_SUCCESS
