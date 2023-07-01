"""
cli.py

Type:       Python Script
Author:     Will Brandon
Created:    June 28, 2023
Revised:    June 30, 2023

The command-line entrypoint for the stax package.
"""

import stax
import argparse as ap
from pywbu.runtime import *


def parse_args(argv: list[str]) -> ap.Namespace:

    parser = ap.ArgumentParser(
        prog=stax.PACK_NAME,
        description='123 abc',
        epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}'
    )

    subparsers = parser.add_subparsers(dest='operation')

    init_parser = subparsers.add_parser('init')
    demolish_parser = subparsers.add_parser('demolish')
    create_parser = subparsers.add_parser('create')
    remove_parser = subparsers.add_parser('remove')
    

    return parser.parse_args(argv[1:])


@main
def main(argv: list[str]) -> int:

    args = parse_args(argv)

    print(args)

    return EXIT_SUCCESS
