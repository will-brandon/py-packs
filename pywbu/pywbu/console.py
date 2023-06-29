"""
console.py

Type:   Python Script
Author: Will Brandon
Date:   June 15, 2023

Contains functionality to interact with the console.
"""

import sys


# Determines whether logging to standard output is enabled and whether output to all streams should
# be formatted.
logging_enabled = True
formatted_output = True


def err(msg: str, exit_code: int=1, spacing: tuple[int, int]=(0, 0)) -> None:
    """
    Displays an error message to the standard error stream and exits with the given exit code. If
    the exit code is None, no exit is performed. By default the exit code is 1. The spacing
    indicates how many extra blank lines will be added above and below the message.
    """

    # Unpack the spacing tuple. Create a string of newline characters for the top and bottom
    # spacing.
    (top_spacing, bottom_spacing) = spacing
    top, bottom = '\n' * top_spacing, '\n' * bottom_spacing

    # Display a formatted error message if formatted output is enabled. Otherwise display an
    # unformatted message.
    if formatted_output:
        print(f'{top}\033[0;91mError:\033[0m {msg}{bottom}', file=sys.stderr)
    else:
        print(f'{top}Error: {msg}{bottom}', file=sys.stderr)

    # If the exit code is not None exit with the given code.
    if exit_code:
        exit(exit_code)


def err_exc(
        exc: BaseException, prefix=None, exit_code: int=None, spacing: tuple[int, int]=(0, 0)
        ) -> None:
    """
    Displays the content of an exception's message as an error message to the standard error stream
    and exits with the given exit code. If the exit code is None, no exit is performed. If the exit
    code is None, no exit is performed. By default the exit code is 1. The spacing indicates how
    many extra blank lines will be added above and below the message.
    """
    
    # If a prefix is proivided and is not empty, prepend it to the exception message.
    msg = f'{prefix}: {exc}' if  prefix and prefix != '' else str(exc)

    # Delegate to the err function.
    warn(msg, exit_code, spacing)


def warn(msg: str, exit_code: int=None, spacing: tuple[int, int]=(0, 0)) -> None:
    """
    Displays a warning message to the standard error stream and exits with the given exit code. If
    the exit code is None, no exit is performed. By default the exit code is None so the program
    will not exit. The spacing indicates how many extra blank lines will be added above and below
    the message.
    """

    # Unpack the spacing tuple. Create a string of newline characters for the top and bottom
    # spacing.
    (top_spacing, bottom_spacing) = spacing
    top, bottom = '\n' * top_spacing, '\n' * bottom_spacing

    # Display a formatted warning message if formatted output is enabled. Otherwise display an
    # unformatted message.
    if formatted_output:
        print(f'{top}\033[0;33mWarning:\033[0m {msg}{bottom}', file=sys.stderr)
    else:
        print(f'{top}Warning: {msg}{bottom}', file=sys.stderr)

    # If the exit code is not None exit with the given code.
    if exit_code:
        exit(exit_code)


def warn_exc(
        exc: BaseException, prefix=None, exit_code: int=None, spacing: tuple[int, int]=(0, 0)
        ) -> None:
    """
    Displays the content of an exception's message as a warning message to the standard error stream
    and exits with the given exit code. If the exit code is None, no exit is performed. By default
    the exit code is None so the program will not exit. The spacing indicates how many extra blank
    lines will be added above and below the message.
    """
    
    # If a prefix is proivided and is not empty, prepend it to the exception message.
    msg = f'{prefix}: {exc}' if  prefix and prefix != '' else str(exc)

    # Delegate to the warn function.
    warn(msg, exit_code, spacing)


def log(msg: str=None, spacing: tuple[int, int]=(0, 0)) -> None:
    """
    Displays a log message if logging is enabled. If the message is None a blank line is displayed.
    The spacing indicates how many extra blank lines will be added above and below the message.
    """

    # Unpack the spacing tuple. Create a string of newline characters for the top and bottom
    # spacing.
    (top_spacing, bottom_spacing) = spacing
    top, bottom = '\n' * top_spacing, '\n' * bottom_spacing
    
    # If logging is enabled display the message.
    if logging_enabled:   
        print(f'{top}{msg if msg else ""}{bottom}')
