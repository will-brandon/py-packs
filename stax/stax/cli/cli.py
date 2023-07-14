"""
cli.py

Type:       Python Script
Author:     Will Brandon
Created:    June 28, 2023
Revised:    July 14, 2023

The command-line entrypoint for the stax package.
"""

import os
from argparse import ArgumentParser, Namespace
from pywbu.runtime import main, EXIT_SUCCESS
import pywbu.console as csl
from pywbu.cli.opset import OperationSet
import stax
from stax.cli.initop import InitOperation
from stax.cli.dismantleop import DismantleOperation
from stax.cli.rootop import RootOperation
from stax.cli.infoop import InfoOperation


def configure_top_level_args(parser: ArgumentParser) -> None:
    """
    Configures the arguments that reside on the top-level argument parser.
    """

    # Add a version argumnt to retreive basic version information.
    parser.add_argument(
        '-V', '--version',
        action='version',
        help='display basic version information and exit',
        version=f'{stax.PACK_NAME} v{stax.PACK_VERSION} by {stax.PACK_AUTHOR}')
    
    # Add an argument to disable warning messages in console output.
    parser.add_argument(
        '-w', '--no-warnings',
        action='store_true',
        help='disable warning messages in console output')

    # Add an argument to disable console log output.
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='disable console output messages')

    # Add an argument to disable formatted console output using ANSI.
    parser.add_argument(
        '-u', '--unformatted',
        action='store_true',
        help='disable console output ANSI formatting')
    
    # Add an argument to specify a path to execute the command other than the current working
    # directory. By default this is the current working directory.
    parser.add_argument(
        '-p', '--path',
        help='run the command from a location instead of the current working directory',
        default=os.getcwd())


def process_top_level_args(args: Namespace) -> None:
    """
    Processed the parsed arguments and performs the appropriate actions.
    """

    # If the no warnings flag is specified disable warnings in console output.
    if args.no_warnings:
        csl.warnings_enabled = False

    # If the quiet flag is specified disable console log output messages.
    if args.quiet:
        csl.logging_enabled = False
    
    # If the unformatted flag is specified disable console output ANSI formatting.
    if args.unformatted:
        csl.formatted_output = False


def parse_args(argv: list[str]) -> None:
    """
    Parses the given list of command-line arguments and performs the appropriate actions.
    """

    # Create the main argument parser.
    parser = ArgumentParser(
        prog=stax.PACK_NAME,
        description='Web module configuration service using Docker Compose.',
        epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}')
    
    # Configure the arguments that reside on the top-level argument parser.
    configure_top_level_args(parser)

    # Create an operation set for the operation positional argument. Add all the relevant operation
    # objects to the set.
    opset = OperationSet('operation')
    opset.add_operations(InitOperation(), DismantleOperation(), RootOperation(), InfoOperation())

    # Configure the parser to use the operations in the operation set.
    opset.configure_parser(parser, True)

    # Parse the arguments into a namespace.
    args = parser.parse_args(argv[1:])

    # Process the top-level arguments.
    process_top_level_args(args)

    # Allow the operation set to process the arguments and perform the proper operation.
    opset.process_args(args)


@main
def main(argv: list[str]) -> int:
    """
    The command-line entrypoint for the stax package.
    """

    # Parse the command-line arguments and perform the appropriate actions.
    parse_args(argv)

    # If the program did not raise an exception or exit by this point it must have succeeded so
    # return a successful exit code.
    return EXIT_SUCCESS


# If this module is executed alone (not as a package) everything should still function properly.
# This is mainly useful for debugging / development to avoid needing to rebuild and reinstall
# everything into pip.
if __name__ == '__main__':
    main()
