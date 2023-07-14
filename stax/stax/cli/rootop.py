"""
rootop.py

Type:       Python Script
Author:     Will Brandon
Created:    July 4, 2023
Revised:    July 14, 2023

Defines a class that represents the command-line display project root operation.
"""

from pathlib import Path
from argparse import ArgumentParser, Namespace
from pywbu.runtime import EXIT_SUCCESS
from pywbu.annotations import override
import pywbu.console as csl
from pywbu.cli.op import Operation
import stax
from stax.project import *


class RootOperation(Operation):
    """
    Represents the command-line display project root operation.
    """

    def __init__(self) -> None:
        """
        Creates a new display project root operation object.
        """

        # Construct the operation parent class with an option name, brief help message, long
        # description, and epilogue.
        super().__init__(
            name='root',
            help='display the path to the project root directory',
            desc='Displays the path to the project root directory in the project tree. This is ' \
                + f'the directory that contains the metadata directory "{PROJ_META_DIR_NAME}".',
            epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}')
    

    @override
    def _configure_args(self, _: ArgumentParser) -> None:
        """
        Configures the arguments of the subparser.
        """

        pass


    @override
    def exec(self, args: Namespace) -> None:
        """
        Executes the operation given a namespace of parsed arguments.
        """

        # Find the enclosing project.
        proj = enclosing_project(Path(args.path))

        # If the project could not be found display a warning and exit.
        if not proj:
            csl.warn(f'No stax project found enclosing "{args.path}".', EXIT_SUCCESS)
        
        # Output the root of the project to the console.
        csl.output(proj.root)            
