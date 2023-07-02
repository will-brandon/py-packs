"""
cliinit.py

Type:       Python Script
Author:     Will Brandon
Created:    July 1, 2023
Revised:    -

Defines the command-line interface and functionality for the init operation.
"""

from argparse import ArgumentParser


def init_parser(parser: ArgumentParser) -> None:

    parser.add_argument('path', default=os.getcwd())

    csl.log('INIT')

    proj.init(Path(args.path))


def dismantle_operation(parser: ArgumentParser) -> None:

    args = parser.parse_args()

    csl.log('DEINIT')

    proj.dismantle(Path(args.path))


def parse_args(argv: list[str]) -> None:

    parser = ArgumentParser(
        prog=stax.PACK_NAME,
        description='123 abc',
        epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}'
    )

    operation_subparsers = parser.add_subparsers(dest='operation')
    init_parser = operation_subparsers.add_parser('init')
    dismantle_parser = operation_subparsers.add_parser('dismantle')

    args = parser.parse_args(argv[1:])

    match args.operation:
        case 'init': init_operation(init_parser)
        case 'dismantle': dismantle_operation(dismantle_parser)
