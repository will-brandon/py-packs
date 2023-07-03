"""
console.py

Type:       Python Script
Author:     Will Brandon
Created:    June 15, 2023
Revised:    July 2, 2023

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

log_ostream = sys.stdout
"""
Determines which output stream log messages will be written to.
"""

warn_ostream = sys.stdout
"""
Determines which output stream warning messages will be written to.
"""

err_ostream = sys.stderr
"""
Determines which output stream error messages will be written to.
"""

confirm_ostream = sys.stdout
"""
Determines which output stream confirmation messages will be written to.
"""

confirm_istream = sys.stdin
"""
Determines which input stream confirmation responses will be read from.
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
        err_ostream.write(f'{top}\033[0;91mError:\033[0m {msg}{bottom}\n')
    else:
        err_ostream.write(f'{top}Error: {msg}{bottom}\n')
    
    # Flush the stream to ensure the message is displayed.
    err_ostream.flush()

    # If the exit code is not None exit with the given code.
    if exit_code != None:
        exit(exit_code)


def err_exc(
        exc: BaseException,
        prefix=None,
        exit_code: int=1,
        spacing: tuple[int, int]=(0, 0)) -> None:
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
        warn_ostream.write(f'{top}\033[0;33mWarning:\033[0m {msg}{bottom}\n')
    else:
        warn_ostream.write(f'{top}Warning: {msg}{bottom}\n')
    
    # Flush the stream to ensure the message is displayed.
    warn_ostream.flush()

    # If the exit code is not None exit with the given code.
    if exit_code != None:
        exit(exit_code)
    
    # Return true indicating that the warning message was successfully written to the stream.
    return True


def warn_exc(
        exc: BaseException,
        prefix=None,
        exit_code: int=None,
        spacing: tuple[int, int]=(0, 0)) -> bool:
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
    
    # Write the message to the appropriate output stream then flush the stream to ensure the message
    # is displayed.
    log_ostream.write(f'{top}{msg if msg else ""}{bottom}\n')
    log_ostream.flush()

    # Return true indicating that the log message was successfully written to the stream.
    return True


def confirm(msg: str=None) -> bool:
    """
    Displays a yes/no confirmation message to the confirmation output stream. The function waits for
    an input line (terminated by a newline character) in the confirmation input stream. The input is
    used to determine whether the message was confirmed ('y' means return true) or denied ('n' or
    anything else means return false).
    """

    # If the message is not None or blank display it.
    if msg and msg != '':
        confirm_ostream.write(f'{msg}\n')
    
    # Write a prompt message to the proper stream then flush the stream to ensure the message is
    # displayed.
    confirm_ostream.write('Confirm (y/n): ')
    confirm_ostream.flush()

    # Read the option from the confirmation input stream and ignore the newline character.
    option = confirm_istream.readline()[:-1]

    # Determine if the specified option was 'y', 'n', or something else.
    match option:

        # If 'y' was specified return true.
        case 'y': return True

        # If 'n' was specified write and flush a cancelation message to the confirmation output
        # stream and return false.
        case 'n':
            confirm_ostream.write('Aborting.\n')
            confirm_ostream.flush()
            return False
        
        # If any other option was specified write and flush a cancelation and invalid option message
        # to the confirmation output stream and return false.
        case _:
            confirm_ostream.write('Invalid option, aborting.\n')
            confirm_ostream.flush()
            return False
