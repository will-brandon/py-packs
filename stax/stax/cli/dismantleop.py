"""
dismantleop.py

Type:       Python Script
Author:     Will Brandon
Created:    July 2, 2023
Revised:    -

Defines a class that represents the command-line project dismantling operation.
"""

import os
from pathlib import Path
from argparse import ArgumentParser, Namespace
from pywbu.annotations import override
import pywbu.console as csl
from pywbu.cli.op import Operation
import stax
import stax.project as proj


class DismantleOperation(Operation):
    """
    Represents the command-line project dismantling operation.
    """


    def __init__(self) -> None:
        """
        Creates a new project dismantling operation object.
        """

        # Construct the operation parent class with an option name, brief help message, long
        # description, and epilogue.
        super().__init__(
            name='dismantle',
            help='removes the stax configuration from a project',
            desc='Removes the stax configuration from a project in the current working directory ' \
                + '(or at a specified directory) deeming the directory no longer a stax project. ' \
                + 'All items inside the directory will be left untouched except for the stax ' \
                + f'metadata subdirectory, "{proj.META_DIR_NAME}".',
            epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}')
    

    @override
    def _configure_args(self, subparser: ArgumentParser) -> None:
        """
        Configures the arguments of the subparser.
        """

        # Add a flag to force the action without confirmation.
        subparser.add_argument(
            '-f', '--force',
            action='store_true',
            help='instructs the program to force the dismantling without a confirmation message')


    @override
    def exec(self, args: Namespace) -> None:
        """
        Executes the operation given a namespace of parsed arguments.
        """

        # Find the root of the project.
        path = proj.root(Path(args.path))

        # Confirm that the user wants to perform this dangerous action unless the force flag was
        # specified.
        if not args.force and not csl.confirm('This will delete project configurations for ' \
                                              + f'"{path}". Are you sure?'):
            return

        # Try to dismantle the project.
        try:
            proj.dismantle(path)
        
        # If an exception is raised just display a warning message.
        except Exception as exc:
            csl.warn_exc(exc)
