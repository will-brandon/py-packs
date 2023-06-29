"""
runtime.py

Type:   Python Script
Author: Will Brandon
Date:   June 29, 2023

Contains functionality to help maintain the program runtime.
"""

import sys
import pywbu.console as csl


# Define default exit codes for indicating success and failure for the runtime of a program.
EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def main(handle_key_interrupt: bool=True) -> object:

    def wrapper(func):

        def inner_wrapper():
            try:
                exit(func(sys.argv))
            except KeyboardInterrupt:

                if handle_key_interrupt:
                    csl.warn('A keyboard interrupt occured.', spacing=(1, 1))
        return inner_wrapper
    
    return wrapper

