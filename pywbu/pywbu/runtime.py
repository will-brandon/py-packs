"""
runtime.py

Type:       Python Script
Author:     Will Brandon
Created:    June 29, 2023
Revised:    -

Contains functionality to help maintain the program runtime.
"""

import sys
import pywbu.console as csl


# Define default exit codes for indicating success and failure for the runtime of a program.
EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def main(func: object) -> object:
    """
    Decorates the entrypoint of a program. The decorated function will be given a list of
    command-line arguments as a parameter. The returned integer value of the decorated function will
    be used as the exit code. If a keyboard interrupt occurs, the exception is caught and a warning
    message is displayed.
    """

    # Create a wrapper function that will be returned.
    def wrapper():
            
            # Try to execute the wrapped function.
            try:
                exit(func(sys.argv))
            
            # If a keyboard interrupt occurs display a warning message.
            except KeyboardInterrupt:
                csl.warn('A keyboard interrupt occured.', spacing=(1, 1))

    # Return the wrapper function.
    return wrapper
