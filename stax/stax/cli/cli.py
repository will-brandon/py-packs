"""
cli.py

Type:       Python Script
Author:     Will Brandon
Created:    June 28, 2023
Revised:    June 30, 2023

The command-line entrypoint for the stax package.
"""

from argparse import ArgumentParser
from pywbu.runtime import *
import stax
from stax.cli.opset import OperationSet
from stax.cli.initop import InitOperation
from stax.cli.dismantleop import DismantleOperation


def parse_args(argv: list[str]) -> None:

    parser = ArgumentParser(
        prog=stax.PACK_NAME,
        description='123 abc',
        epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}'
    )

    opset = OperationSet('operation')
    opset.add_operations(InitOperation(), DismantleOperation())
    opset.configure_parser(parser)

    args = parser.parse_args(argv[1:])

    print(args)


from abc import ABC

@main
def main(argv: list[str]) -> int:

    parse_args(argv)

    return EXIT_SUCCESS


if __name__ == '__main__':
    main()
