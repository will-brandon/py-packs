"""
configop.py

Type:       Python Script
Author:     Will Brandon
Created:    July 6, 2023
Revised:    -

Defines a class that represents the command-line configuraton management operation.
"""

from pathlib import Path
import json
from argparse import ArgumentParser, Namespace
from pywbu.runtime import EXIT_SUCCESS
from pywbu.annotations import override
import pywbu.console as csl
from pywbu.cli.op import Operation
import stax
import stax.project as proj
import stax.config as cfg


JSON_INDENT = 2
"""
The level of indent to use for formatting JSON. A value of None will not format the JSON at all. A
value of 0 will insert newlines but no indentation.
"""


class ConfigOperation(Operation):
    """
    Represents the command-line configuraton management operation.
    """

    def __init__(self) -> None:
        """
        Creates a new configuraton management operation object.
        """

        # Construct the operation parent class with an option name, brief help message, long
        # description, and epilogue.
        super().__init__(
            name='config',
            help='show the configuration model as JSON',
            desc='Shows the configuration model inside the metadata directory. The model object ' \
                + 'is displayed as JSON in console output. This is ideal for APIs.',
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

        # Find the root of the project.
        root = proj.root(Path(args.path))

        # If the project root could not be found display a warning and exit.
        if not root:
            csl.warn(f'No stax project found enclosing "{args.path}".', EXIT_SUCCESS)

        # Read the model object from the configuration file.
        model = cfg.read_in_proj(root)
        
        # Output the json configuration model to the console.
        csl.output(json.dumps(model, indent=JSON_INDENT))
