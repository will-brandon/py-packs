"""
infoop.py

Type:       Python Script
Author:     Will Brandon
Created:    July 6, 2023
Revised:    -

Defines a class that represents the command-line project information operation.
"""

from pathlib import Path
from argparse import ArgumentParser, Namespace
from pywbu.runtime import EXIT_SUCCESS
from pywbu.annotations import override
import pywbu.console as csl
from pywbu.cli.op import Operation
import stax
import stax.project as proj
import stax.config as cfg


class InfoOperation(Operation):
    """
    Represents the command-line project information operation.
    """

    def __init__(self) -> None:
        """
        Creates a new project information operation object.
        """

        # Construct the operation parent class with an option name, brief help message, long
        # description, and epilogue.
        super().__init__(
            name='info',
            help='show information about the project',
            desc='Shows useful information about the project such as its name, author, creation ' \
                + 'date, module info, etc.',
            epilog=f'{stax.PACK_AUTHOR} | {stax.PACK_CREATION}')
    

    @override
    def _configure_args(self, subparser: ArgumentParser) -> None:
        """
        Configures the arguments of the subparser.
        """

        pass


    @override
    def exec(self, args: Namespace) -> None:
        """
        Executes the operation given a namespace of parsed arguments.
        """

        # Find the root of the project.
        root = proj.root(Path(args.path))

        # If the project root could not be found display a warning and exit.
        if not root:
            csl.warn(f'No stax project found enclosing "{args.path}".', EXIT_SUCCESS)

        # Read the model object from the configuration file.
        model = cfg.read_in_proj(root)
        
        # Output the json configuration model to the console.
        csl.output(f'Location: {root}')
        csl.output(f'UUID:     {model["uuid"]}')
        csl.output(f'Name:     {model["name"]}')
        csl.output(f'Author:   {model["author"]}')
        csl.output(f'Created:  {model["creation_date"]}')
        csl.output(f'Modules:  {len(model["modules"])}')
