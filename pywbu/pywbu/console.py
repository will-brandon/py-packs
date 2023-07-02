"""
console.py

Type:       Python Script
Author:     Will Brandon
Created:    June 15, 2023
Revised:    June 30, 2023

Contains functionality to interact with the console.
"""

import sys


logging_enabled = True
"""
Determines whether log output is enabled.
"""

warnings_enabled = True
"""
Determines whether warnings are enabled.
"""

formatted_output = True
"""
Determines whether output should be written to streams with ANSI format codes.
"""

log_stream = sys.stdout
"""
Determines which stream log messages will be written to.
"""

warn_stream = sys.stdout
"""
Determines which stream warning messages will be written to.
"""

err_stream = sys.stderr
"""
Determines which stream error messages will be written to.
"""


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
        err_stream.write(f'{top}\033[0;91mError:\033[0m {msg}{bottom}\n')
    else:
        err_stream.write(f'{top}Error: {msg}{bottom}\n')

    # If the exit code is not None exit with the given code.
    if exit_code:
        exit(exit_code)


def err_exc(
        exc: BaseException, prefix=None, exit_code: int=1, spacing: tuple[int, int]=(0, 0)
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
    err(msg, exit_code, spacing)


def warn(msg: str, exit_code: int=None, spacing: tuple[int, int]=(0, 0)) -> bool:
    """
    Displays a warning message to the standard error stream and exits with the given exit code. If
    the exit code is None, no exit is performed. By default the exit code is None so the program
    will not exit. The spacing indicates how many extra blank lines will be added above and below
    the message. Returns true if and only if warnings are enabled.
    """

    # If warning messages are not enabled immediately return false.
    if not warnings_enabled:
        return False

    # Unpack the spacing tuple. Create a string of newline characters for the top and bottom
    # spacing.
    (top_spacing, bottom_spacing) = spacing
    top, bottom = '\n' * top_spacing, '\n' * bottom_spacing

    # Display a formatted warning message if formatted output is enabled. Otherwise display an
    # unformatted message.
    if formatted_output:
        warn_stream.write(f'{top}\033[0;33mWarning:\033[0m {msg}{bottom}\n')
    else:
        warn_stream.write(f'{top}Warning: {msg}{bottom}\n')

    # If the exit code is not None exit with the given code.
    if exit_code:
        exit(exit_code)
    
    # Return true indicating that the warning message was successfully written to the stream.
    return True


def warn_exc(
        exc: BaseException, prefix=None, exit_code: int=None, spacing: tuple[int, int]=(0, 0)
        ) -> bool:
    """
    Displays the content of an exception's message as a warning message to the standard error stream
    and exits with the given exit code. If the exit code is None, no exit is performed. By default
    the exit code is None so the program will not exit. The spacing indicates how many extra blank
    lines will be added above and below the message. Returns true if and only if warnings are
    enabled.
    """
    
    # If a prefix is proivided and is not empty, prepend it to the exception message.
    msg = f'{prefix}: {exc}' if  prefix and prefix != '' else str(exc)

    # Delegate to the warn function.
    return warn(msg, exit_code, spacing)


def log(msg: str=None, spacing: tuple[int, int]=(0, 0)) -> bool:
    """
    Displays a log message if logging is enabled. If the message is None a blank line is displayed.
    The spacing indicates how many extra blank lines will be added above and below the message.
    Returns true if and only if logging is enabled.
    """

    # If logging is not enabled immediately return false.
    if not logging_enabled: 
        return False

    # Unpack the spacing tuple. Create a string of newline characters for the top and bottom
    # spacing.
    (top_spacing, bottom_spacing) = spacing
    top, bottom = '\n' * top_spacing, '\n' * bottom_spacing
    
    # Write the message to the appropriate output stream and return true indicating that the log
    # message was successfully written to the stream.
    log_stream.write(f'{top}{msg if msg else ""}{bottom}\n')
    return True
