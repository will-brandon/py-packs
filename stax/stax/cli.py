"""
cli.py

Type:       Python Script
Author:     Will Brandon
Created:    June 28, 2023
Revised:    June 30, 2023

The command-line entrypoint for the stax package.
"""

import os
from pathlib import Path
from argparse import ArgumentParser
from pywbu.runtime import *
import stax
import stax.project as proj


def parse_args(argv: list[str]) -> None:

    parser = ArgumentParser(
        prog=stax.PACK_NAME,
        description='123 abc',
        epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}'
    )

    operation_subparsers = parser.add_subparsers(dest='operation', required=True)
    init_parser = operation_subparsers.add_parser('init')
    dismantle_parser = operation_subparsers.add_parser('dismantle')

    init_parser.add_argument('path', nargs=1, default=os.getcwd())
    dismantle_parser.add_argument('path', nargs=1, default=os.getcwd())

    args = parser.parse_args(argv[1:])

    match args.operation:
        case 'init': proj.init(Path(args.path))
        case 'dismantle': proj.dismantle(Path(args.path))


@main
def main(argv: list[str]) -> int:

    parse_args(argv)

    return EXIT_SUCCESS


if __name__ == '__main__':
    main()
