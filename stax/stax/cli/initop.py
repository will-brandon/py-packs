"""
initop.py

Type:       Python Script
Author:     Will Brandon
Created:    July 2, 2023
Revised:    -

Defines a class that represents the command-line project initialization operation.
"""

import os
from pathlib import Path
from argparse import ArgumentParser, Namespace
from pywbu.annotations import override
import pywbu.console as csl
from pywbu.cli.op import Operation
import stax
import stax.project as proj


class InitOperation(Operation):
    """
    Represents the command-line project initialization operation.
    """


    def __init__(self) -> None:
        """
        Creates a new project initialization operation object.
        """

        # Construct the operation parent class with an option name, brief help message, long
        # description, and epilogue.
        super().__init__(
            name='init',
            help='creates a new stax project',
            desc='Creates a new stax project in the current working directory (or at a specified ' \
                + 'directory). The content of the directory becomes part of the project. A ' \
                + f'metadata subdirectory, "{proj.META_DIR_NAME}", will be created.',
            epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}'
        )


    @override
    def _configure_args(self, subparser: ArgumentParser) -> None:
        """
        Configures the arguments of the subparser.
        """

        # Add a project directory path argument that defaults to the current working directory.
        subparser.add_argument('path', nargs='?', default=os.getcwd())


    @override
    def exec(self, args: Namespace) -> None:
        """
        Executes the operation given a namespace of parsed arguments.
        """

        # Try to initialize the project.
        try:
            proj.init(Path(args.path))
        
        # If an exception is raised just display a warning message.
        except Exception as exc:
            csl.warn_exc(exc)
