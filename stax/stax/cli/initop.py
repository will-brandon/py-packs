"""
initop.py

Type:       Python Script
Author:     Will Brandon
Created:    July 2, 2023
Revised:    -

Defines an init operation class which represents the command-line init operation.
"""

import os
from pathlib import Path
from argparse import ArgumentParser, Namespace
import pywbu.console as csl
import stax.project as proj
from stax.cli.op import Operation


class InitOperation(Operation):


    def __init__(self) -> None:
        super().__init__('init')


    def _configure_args(self, subparser: ArgumentParser) -> None:

        subparser.add_argument('path', nargs='?', default=os.getcwd())

    
    def exec(self, parsed_args: Namespace) -> None:

        try:

            proj.init(Path(parsed_args.path))
        
        except Exception as exc:

            csl.err_exc(exc)
