"""
infoop.py

Type:       Python Script
Author:     Will Brandon
Created:    July 6, 2023
Revised:    July 14, 2023

Defines a class that represents the command-line project information operation.
"""

from pathlib import Path
import json
from argparse import ArgumentParser, Namespace
from pywbu.runtime import EXIT_SUCCESS
from pywbu.annotations import override
import pywbu.console as csl
from pywbu.cli.op import Operation
import stax
from stax.project import *


JSON_INDENT = 2
"""
The level of indent to use for formatting JSON. A value of None will not format the JSON at all. A
value of 0 will insert newlines but no indentation.
"""


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

        subparser.add_argument(
            '-j', '--json',
            action='store_true',
            help='display the info model as JSON')


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

        # Read the model object from the configuration file.
        model = proj.config().model()

        # If the JSON argument is specified, output the model as a formatted JSON string and return.
        if (args.json):
            csl.output(json.dumps(model, indent=JSON_INDENT))
            return
        
        # Output the json configuration model to the console.
        csl.output(f'Location: {proj.root}')
        csl.output(f'UUID:     {model["uuid"]}')
        csl.output(f'Name:     {model["name"]}')
        csl.output(f'Modules:  {len(model["modules"])}')
        csl.output(f'Created:  {model["creation_date"]}')
        
        # If an author was specified, display the author.
        if model['author']:
            csl.output(f'Author:   {model["author"]}')
        
        # If a description was specified, display the description.
        if model['desc']:
            csl.output(f'\n{model["desc"]}')
