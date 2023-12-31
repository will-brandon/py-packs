"""
runtime.py

Type:       Python Script
Author:     Will Brandon
Created:    June 29, 2023
Revised:    -

Contains functionality to help maintain the program runtime.
"""

from typing import Callable
import sys
import pywbu.console as csl


EXIT_SUCCESS = 0
"""
0, an exit code widely accepted as indicating a successful program execution.
"""

EXIT_FAILURE = 1
"""
1, an exit code widely accepted as indicating an erroneous program execution.
"""


def main(func: Callable[[list[str]], int]) -> Callable[[], None]:
    """
    Decorates the entrypoint of a program. The decorated function will be given a list of
    command-line arguments as a parameter. The returned integer value of the decorated function will
    be used as the exit code. If a keyboard interrupt occurs, the exception is caught and a warning
    message is displayed.
    """

    # Create a wrapper function that will be returned.
    def wrapper() -> None:
            
            # Try to execute the wrapped function.
            try:
                exit(func(sys.argv))
            
            # If a keyboard interrupt occurs display a warning message.
            except KeyboardInterrupt:
                csl.warn('A keyboard interrupt occured.', spacing=(1, 1))

    # Return the wrapper function.
    return wrapper
