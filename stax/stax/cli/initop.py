"""
initop.py

Type:       Python Script
Author:     Will Brandon
Created:    July 2, 2023
Revised:    July 14, 2023

Defines a class that represents the command-line project initialization operation.
"""

from pathlib import Path
from argparse import ArgumentParser, Namespace
from pywbu.annotations import override
import pywbu.console as csl
from pywbu.cli.op import Operation
import stax
from stax.project import *


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
            help='create a new stax project',
            desc='Creates a new stax project in the current working directory (or at a specified ' \
                + 'directory). The content of the directory becomes part of the project. A ' \
                + f'metadata subdirectory, "{PROJ_META_DIR_NAME}", will be created.',
            epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}')


    @override
    def _configure_args(self, subparser: ArgumentParser) -> None:
        """
        Configures the arguments of the subparser.
        """

        # Add optional arguments to specify a project name, author, and descripton.
        subparser.add_argument('-n', '--name', default=None, help='the title of the project')
        subparser.add_argument('-a', '--author', default=None, help='the author of the project')
        subparser.add_argument('-d', '--desc', default=None, help='a description of the project')


    @override
    def exec(self, args: Namespace) -> None:
        """
        Executes the operation given a namespace of parsed arguments.
        """

        # Create a path object.
        path = Path(args.path)

        # If the path already points to a stax project display a warning and return immediately.
        if is_project(path):
            csl.warn(f'The given path already points to a stax project: "{path}".')
            return

        # Try to initialize the project.
        try:
            create_project(path, args.name, args.author, args.desc)
        
        # If an exception is raised just display a warning message.
        except Exception as exc:
            csl.warn_exc(exc)
